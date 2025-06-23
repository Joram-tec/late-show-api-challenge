from server.extensions import db, migrate, jwt

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer,primary_key=True)
    rating = db.Column(db.Integer)
    
    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"))
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"))

    guest = db.relationship("Guest", back_populates="appearances")
    episode = db.relationship("Episode", back_populates="appearances")


    __table_args__ = (db.CheckConstraint("rating>=1 AND rating <=5", name = "valid_rating"),)