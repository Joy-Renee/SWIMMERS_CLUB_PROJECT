from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, Swimmer, Coach, Team, Event, TrainingSession

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///swimmersClub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'

db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "<h1>Swim Club Management System</h1>"


if __name__ == '__main__':
    app.run(debug=True)
