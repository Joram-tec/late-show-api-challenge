from datetime import date
from sqlalchemy import Date
from server.extensions import db, migrate, jwt


class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Date)
    number = db.Column(db.Integer)

    appearances = db.relationship('Appearance', back_populates = "episode", cascade="all,delete")

    def __repr__(self):
        return {self.id}, {self.date}, {self.number}