from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()


class Gender(enum.Enum):
    male = 'male'
    female = 'female'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    # gender = db.Column(db.String(3), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    id_facultet = db.Column(db.Integer, db.ForeignKey('facultet.id'), nullable=False)

    def __repr__(self):
        return f'Студент({self.lastname} {self.firstname}, {self.id_facultet}/{self.group})'


class Facultet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_facultet = db.Column(db.String(100), unique=True, nullable=False)
    students = db.relationship('Student', backref=db.backref('facultet'), lazy=True)

    def __repr__(self):
        return f'Факультет {self.name_facultet}'
