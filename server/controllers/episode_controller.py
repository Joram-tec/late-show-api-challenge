from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.extensions import db

episode_blues = Blueprint("episode_blues", __name__)

@episode_blues.route("/",methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify ([{"id":epi.id, "date": epi.date, "number":epi.number} for epi in episodes ]), 200

@episode_blues.route("/<int:id>",methods=["GET"])
def get_episodes_by_id(id):
    epi = Episode.query.get_or_404(id)
    appearances =[{
        "id":appearance.id, 
        "rating":appearance.rating, 
        "guest":{
            "id":appearance.guest_id, 
            "name":Guest.query.get(appearance.guest_id).name}} for appearance in epi.appearances]

    return jsonify ({
        "id": epi.id,
        "date":epi.date, 
        "number":epi.number, 
        "appearances":appearances
        }),200       

@episode_blues.route("/<int:id>",methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get(id)
    if not ep:
        return jsonify({"error": "Episode Invalid!"}), 404

    db.session.delete(ep)
    db.session.commit()
    return "", 204