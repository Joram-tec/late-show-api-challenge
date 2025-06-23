from flask import Blueprint,jsonify
from server.models.guest import Guest
from server.extensions import db

guest_blues = Blueprint("guest_blues",__name__) 

@guest_blues.route("/",methods=["GET"])
def guest_list():
    guests= Guest.query.all()
    guest_lists = [{"id":guest.id, "name":guest.name, "occupation":guest.occupation}for guest in guests]

    return jsonify(guest_lists), 200