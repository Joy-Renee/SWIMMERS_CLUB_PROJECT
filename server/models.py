from flask_sqlalchemy import SQLAlchemy
from datetime import date, time

db = SQLAlchemy()


class Swimmer(db.Model):
    __tablename__ = 'swimmers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False )
    age = db.Column(db.Integer, nullable=False)
    swimming_style = db.Column(db.String, nullable=False)
    best_lap = db.Column(db.Float, nullable=False)
    experience = db.Column(db.Float, nullable=False)

    coach_id = db.Column(db.Integer, db.ForeignKey('coaches.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    coach = db.relationship("Coach", back_populates="swimmer")
    team = db.relationship('Team', back_populates='swimmers')

class Coach(db.Model):
    __tablename__ = 'coaches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.Float, nullable=False)
    expertise = db.Column(db.String, nullable=False)

    swimmer_id = db.Column(db.Integer, db.ForeignKey('swimmers.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    swimmer = db.relationship("Swimmer", back_populates="coaches")
    team = db.relationship('Team', back_populates='coaches')

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    swimmer_id = db.Column(db.Integer, db.ForeignKey('swimmers.id'))
    coach_id = db.Column(db.Integer, db.ForeignKey('coaches.id'))

    coach = db.relationship('Coach', back_populates='teams')
    swimmer = db.relationship('Swimmer', back_populates='teams')
    event = db.relationship('Event', back_populates='teams', cascade='all, delete-orphan')
    trainingSession = db.relationship('TrainingSession', back_populates='teams', cascade='all, delete-orphan')


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String(100), nullable=True)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    team = db.relationship('Team', back_populates='events', cascade='all, delete-orphan')

class TrainingSession(db.Model):
    __tablename__ = 'trainingSessions'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=True)
    time = db.Column(db.Time, nullable=True)
    description = db.Column(db.String(100), nullable=True)
    coach_id = db.Column(db.Integer, db.ForeignKey('coaches.id'))

    team = db.relationship('Team', back_populates='trainingSessions', cascade='all, delete-orphan')








