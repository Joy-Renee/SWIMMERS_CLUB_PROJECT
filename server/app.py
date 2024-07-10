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
migrate = Migrate(app, db, render_as_batch=True)

@app.route('/')
def home():
    return "<h1>Swim Club Management System</h1>"

@app.route('/swimmers', methods=['GET', 'POST'])
def swimmers():
    if request.method == 'GET':
        swimmers = Swimmer.query.all()
        return jsonify([swimmer.serialize() for swimmer in swimmers])
    elif request.method == 'POST':
        data = request.get_json()
        new_swimmer = Swimmer(name=data['name'], age=data['age'], swimming_style=data['swimming_style'], best_lap=data['best_lap'], experience=data['experience'])
        db.session.add(new_swimmer)
        db.session.commit()
        return jsonify(new_swimmer.serialize()), 201

if __name__ == '__main__':
    app.run(debug=True)
