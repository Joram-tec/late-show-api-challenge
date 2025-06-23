from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.extensions import db
from server.models.appearance import Appearance

appearance_blues = Blueprint("appearance_blues", __name__)


@appearance_blues.route("/", methods=["GET"])
def list_appearances():
    appearances = Appearance.query.all()
    return jsonify([
        {
            "id": a.id,
            "rating": a.rating,
            "guest_id": a.guest_id,
            "episode_id": a.episode_id
        } for a in appearances
    ]), 200


@appearance_blues.route("/",methods=["POST"])
@jwt_required()
def create_appearance():
    datas = request.get_json()
    new_appearance = Appearance(
        rating=datas["rating"],
        guest_id=datas["guest_id"],
        episode_id=datas["episode_id"]
    )
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify({"message": "Appearance created Successfully!"}), 201
