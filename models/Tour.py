from datetime import datetime
from ICT239_qns2b import app, db
from models.Schedule import Schedule

all_Tours = [{"code": "VE001", "country": "Vietnam", "name": "Sapa Halong Hanoi", "cost": 650,
                  "description": "Luxury overnight cruise in Halong bay, beautiful rice terraces and mountains of Sapa & vibrant Hanoi are customized for best holiday to Vietnam from Singapore. It can be customizedfor active travelers",
                  "days": 6, "nights": 5, "url": "https://www.deluxevietnamtours.com/images/mucangchai1.jpg",
                  "schedule": [{"departureDate": datetime(2024, 9, 15), "capacity": 5},
                               {"departureDate": datetime(2024, 10, 18), "capacity": 5}]},
                 {"code": "VE002", "country": "Vietnam", "name": "Halong Bay Hanoi Tour", "cost": 450,
                  "description": "Charming Hanoi and amazing Halong bay UNESCO site - top of the very best Vietnam tours from Singapore for family holidays with kids, seniors, teenagers or active travelers.",
                  "days": 5, "nights": 4, "url": "https://www.deluxevietnamtours.com/photo/halong6.jpg",
                  "schedule": [{"departureDate": datetime(2024, 9, 15), "capacity": 4}]},
                 {"code": "IN001", "country": "Indonesia", "name": "Labuan Bajo Escapade", "cost": 699,
                  "description": "Discover Labuan Bajo, an Indonesian gem boasting stunning landscapes and vibrant marine life. Trek through Komodo National Park to encounter the famed Komodo dragons, dive into crystal-clear waters teeming with colorful reefs, and immerse yourself in local culture. End your days with breathtaking sunsets over the archipelago, making memories that will last a lifetime.",
                  "days": 4, "nights": 3,
                  "url": "https://www.wtstravel.com.sg/wp-content/uploads/2024/04/Padar-Island.jpg",
                  "schedule": [{"departureDate": datetime(2024, 9, 16), "capacity": 6},
                               {"departureDate": datetime(2024, 10, 19), "capacity": 4}]},
                 {"code": "IN002", "country": "Indonesia", "name": "The City of Flower Bandung", "cost": 600,
                  "description": "Discover the captivating beauty of Bandung. Immerse yourself in the rich culture, vibrant markets, and scenic landscapes of this Indonesian gem. Explore Bandung's unique blend of tradition and modernity with our curated packages.",
                  "days": 5, "nights": 4,
                  "url": "https://www.wtstravel.com.sg/wp-content/uploads/2023/12/Ranca-Upas-Deer-Conservation.png",
                  "schedule": [{"departureDate": datetime(2024, 10, 19), "capacity": 8}]},
                 {"code": "US001", "country": "USA", "name": "Jewels of Alaska", "cost": 4500,
                  "description": "Begin your adventure in Anchorage with a sweet treat: Taste agutak — Inuit Ice Cream — after an exclusive demonstration by Alaska's Indigenous people at the Alaska Native Heritage Center. Board a jet boat for a tour along the Chulitna River to a trapper’s cabin, where you will learn about the lifestyle of hunting and trapping in the state. Ride along the world-famous, glass- domed Alaskan Railroad toward Denali National Park, where the country’s tallest peak, Mount McKinley, will greet you. Meet the champion dog team of a four-time Iditarod winner and allow him to regale you with tales of the 1,049-mile dogsled race over lunch at his home. From Whittier, take a 100-mile boat tour of Prince William Sound and the see the glaciers of College Fjord.",
                  "days": 7, "nights": 6,
                  "url": "https://www.insightvacations.com/media/bdbbp0rn/alaska-range-alkeetna-alaska-16.jpg",
                  "schedule": [{"departureDate": datetime(2024, 11, 23), "capacity": 15}]},
                 {"code": "US002", "country": "USA", "name": "Wonders of the American West", "cost": 5200,
                  "description": "Travel to Bryce Canyon National Park to explore its rock pillars and natural amphitheatres — then feast with your fellow travelers overlooking the park’s iconic orange rock formations. In Moab, see the ancient pueblo dwellings in Mesa Verde National Park, where the Ancestral Pueblo people once lived. Meet a Navajo guide in Monument Valley Navajo Tribal Park, where you will board ATVs, explore the valley and learn about the tribe’s history. Later, eat a traditional Navajo meal amid the valley’s beautiful buttes and mesas. Highlights include the picturesque Lake Powell, the Glen Canyon Da and the Grand Canyon National Park.",
                  "days": 10, "nights": 9,
                  "url": "https://www.insightvacations.com/media/csdf5ien/scenic-drive-along-desert-view-drive-arizona-1.jpg",
                  "schedule": [{"departureDate": datetime(2024, 10, 26), "capacity": 12}]},
                 {"code": "CH001", "country": "China", "name": "Odyssey of the Yangtze", "cost": 1800,
                  "description": "Witness the contrast of China’s old and new in Beijing, Xi’an, Chongqing and Shanghai as you visit sights of great historical and cultural significance. Beijing highlights: Tiananmen Square, Forbidden City, Summer Palace, and the Great Wall. Lively and lovely, Xi’an will surprise and delight with its more relaxed vibe, delicious food, and diverse cultural influences found in places like Muslim Quarter, the Great Mosque, and Xi’an Ancient City Wall. Visit Chongqing, the booming mega city. Enjoy three nights cruising the Yangtze River between Chongqing and Yichang viewing spectacular gorges including Qutang Gorge and Wu Gorge. Travel to Shanghai with highlights like The Bund, Yuyuan Garden, and more.",
                  "days": 12, "nights": 11,
                  "url": "https://www.pacificholidaysinc.com/assets/images/Destinations/Asia/China/Cities/Yangtze-river/_015.jpg",
                  "schedule": [{"departureDate": datetime(2024, 9, 21), "capacity": 6},
                               {"departureDate": datetime(2024, 10, 26), "capacity": 8}]},
                 {"code": "CH002", "country": "China", "name": "Grand China with Pandas", "cost": 2300,
                  "description": "The adventure begins in bustling Beijing, China’s capital. Explore iconic landmarks like the Forbidden City, Summer Palace, and the Great Wall. Start your journry along the Silk Road. In Chengdu, enjoy Sichuan hospitality and a traditional hotpot. Spend time with the gorgeous giant pandas at the Dujiangyan Panda Base. Work as a panda keeper and enjoy the truly unique experience. Spend three incredible days cruising the Yangtze River and be enchanted by the impressive gorges, mountains, and surrounding terrain. Explore Shanghai old and new, including The Bund, Yuyuan Garden, and Sinan Road in the Former French Concession.",
                  "days": 13, "nights": 12,
                  "url": "https://cdn.chinadialogue.net/content/uploads/2020/05/20091014/2400-china_Panda_Nation.jpg",
                  "schedule": [{"departureDate": datetime(2024, 9, 18), "capacity": 8},
                               {"departureDate": datetime(2024, 10, 19), "capacity": 10}]}]

class Tour(db.Document):
    meta = {'collection':'tours'}

    code = db.StringField(unique=True, required=True)
    name = db.StringField(required=True)
    country = db.StringField()
    cost = db.FloatField(required=True)
    description = db.StringField()
    days = db.IntField(required=True) # int because might need to do calculation with it such as cost * duration later on
    nights = db.IntField(required=True)
    url = db.StringField()
    schedule = db.ListField(db.ReferenceField(Schedule)) #List of Schedule document references

    @staticmethod
    def getTour(code):
        tour = Tour.objects(code=code).first()
        if tour is None: #Tour document does not exist in collection yet
            for tourData in all_Tours: #Find the tour that matches this tour
                if tourData['code'] == code:
                    scheduleList = []
                    for scheduleData in tourData['schedule']: # iterates through schedules
                        newSchedule = Schedule.createSchedule(scheduleData['departureDate'], scheduleData['capacity'])
                        scheduleList.append(newSchedule)
                    newTour = Tour.createTour(
                        code=tourData['code'],
                        name=tourData['name'],
                        country=tourData['country'],
                        cost=tourData['cost'],
                        description=tourData['description'],
                        days=tourData['days'],
                        nights=tourData['nights'],
                        url=tourData['url'],
                        schedule=scheduleList)
                    return newTour
            return None
        else:
            return tour

    @staticmethod
    def getAllTours():
        tours = []
        for tour in all_Tours: #iterate through all_Tours
            getTour = Tour.getTour(tour['code']) #gets the tour if already exists, else creates a new one
            tours.append(getTour)
        return tours

    @staticmethod
    def createTour(code, name, country, cost, description, days, nights, url, scheduleList = []):
        return Tour(code=code, name=name, country=country, cost=cost, description=description, days=days, nights=nights, url=url, schedule=scheduleList).save()