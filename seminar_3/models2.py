from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    id_author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.title}, {self.year}.'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    authors = db.relationship('Book', backref=db.backref('author'), lazy=True)

    def __repr__(self):
        return f'{self.id}: {self.lastname} {self.firstname}'
