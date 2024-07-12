from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError 
from sqlalchemy.orm.exc import NoResultFound
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

@app.route('/swimmers', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def swimmers():
    if request.method == 'GET':
        swimmers = Swimmer.query.all()
        return jsonify([swimmer.serialize() for swimmer in swimmers])

    elif request.method == 'POST':
        data = request.get_json()
        new_swimmer = Swimmer(
            name=data['name'],
            age=data['age'],
            swimming_style=data['swimming_style'],
            best_lap=data['best_lap'],
            experience=data['experience'],
            coach_id=data.get('coach_id'),
            team_id=data.get('team_id')
        )
        db.session.add(new_swimmer)
        db.session.commit()
        return jsonify(new_swimmer.serialize()), 201

    elif request.method == 'PATCH':
        data = request.get_json()
        swimmer = Swimmer.query.get(data['id'])
        if not swimmer:
            return make_response(jsonify({'error': 'Swimmer not found'}), 404)
        
        if 'name' in data:
            swimmer.name = data['name']
        if 'age' in data:
            swimmer.age = data['age']
        if 'swimming_style' in data:
            swimmer.swimming_style = data['swimming_style']
        if 'best_lap' in data:
            swimmer.best_lap = data['best_lap']
        if 'experience' in data:
            swimmer.experience = data['experience']
        if 'coach_id' in data:
            swimmer.coach_id = data['coach_id']
        if 'team_id' in data:
            swimmer.team_id = data['team_id']

        db.session.commit()
        return jsonify(swimmer.serialize()), 200
    
    elif request.method == 'DELETE':
        data = request.get_json()
        swimmer = Swimmer.query.get(data['id'])
        if not swimmer:
            return make_response(jsonify({'error': 'Swimmer not found'}), 404)

        db.session.delete(swimmer)
        db.session.commit()
        return '', 204

@app.route('/coaches', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def coaches():
    if request.method == 'GET':
        coaches = Coach.query.all()
        return jsonify([coach.serialize() for coach in coaches])
    elif request.method == 'POST':
        data = request.get_json()
        new_coach =  Coach(name=data['name'], age=data['age'], experience=data['experience'], expertise=data['expertise'])
        db.session.add(new_coach)
        db.session.commit()
        return jsonify(new_coach.serialize()), 201
    
    elif request.method == 'PATCH':
        data = request.get_json()
        coach = Coach.query.get(data['id'])
        if not coach:
            return make_response(jsonify({'error': 'Coach not found'}), 404)
        
        if 'name' in data:
            coach.name = data['name']
        if 'age' in data:
            coach.age = data['age']
        if 'experience' in data:
            coach.experience = data['experience']
        if 'expertise' in data:
            coach.expertise = data['expertise']
        if 'team_id' in data:
            coach.team_id = data['team_id']

        db.session.commit()
        return jsonify(coach.serialize()), 200
    
    elif request.method == 'DELETE':
        data = request.get_json()
        coach = Coach.query.get(data['id'])
        if not coach:
            return make_response(jsonify({'error': 'Coach not found'}), 404)

        db.session.delete(coach)
        db.session.commit()
        return '', 204
    
@app.route('/teams', methods=['GET', 'POST'])
def teams():
    if request.method == 'GET':
        teams = Team.query.all()
        return jsonify([team.serialize() for team in teams])

    elif request.method == 'POST':
        data = request.get_json()
        new_team = Team(name=data['name'])
        db.session.add(new_team)
        db.session.commit()
        return jsonify(new_team.serialize()), 201
    #crud for events#
@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'GET':
        events = Event.query.all()
        return jsonify([event.serialize() for event in events])
    elif request.method == 'POST':
        data = request.get_json()
        try:
            new_event = Event(
                name=data['name'],
                description=data['description']
            )
            db.session.add(new_event)
            db.session.commit()
            return jsonify(new_event.serialize()), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": "Data integrity error"}), 400

@app.route('/events/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def event_detail(id):
    try:
        event = Event.query.get_or_404(id)
        if request.method == 'GET':
            return jsonify(event.serialize())
        elif request.method == 'PUT':
            data = request.get_json()
            event.name = data.get('name', event.name)
            event.description = data.get('description', event.description)
            db.session.commit()
            return jsonify(event.serialize())
        elif request.method == 'DELETE':
            db.session.delete(event)
            db.session.commit()
            return jsonify({"message": "Event deleted"}), 200
    except NoResultFound:
        return jsonify({"error": "Event not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
