from server.extensions import db, migrate, jwt
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String,nullable=False)

    def set_pass(self,password):
        self.password_hash =generate_password_hash(password) 

    def check_pass(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"

