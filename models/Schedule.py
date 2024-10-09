from ICT239_qns2b import app, db


class Schedule(db.Document):
    meta = {'collection': 'schedules'}
    departureDate = db.DateTimeField(required=True)
    capacity = db.IntField(required=True)
    availableSeats = db.IntField(required=True)

    @staticmethod
    def createSchedule(departureDate, capacity):
        return Schedule(departureDate=departureDate, capacity=capacity, availableSeats=capacity).save()

    @staticmethod
    def getSchedule(id):
        return Schedule.objects(id=id).first()