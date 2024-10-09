from flask import Flask
from flask_mongoengine import MongoEngine, Document

def create_app():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'tours',
        'host': 'localhost'
    }
    app.static_folder = "static"
    db = MongoEngine(app)
    return app, db

app, db = create_app()