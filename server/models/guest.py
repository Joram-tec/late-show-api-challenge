from server.extensions import db, migrate, jwt


class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    occupation = db.Column(db.String)


    appearances = db.relationship('Appearance', back_populates='guest')

    def __repr__(self):
        return f"<Guest {self.id}: {self.name}, {self.occupation}>"
