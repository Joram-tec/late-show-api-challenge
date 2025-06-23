from flask import Blueprint, request, jsonify
from server.models.user import User
from server.extensions import db
from flask_jwt_extended import create_access_token


auth_blues = Blueprint("auth_blues",__name__)

@auth_blues.route("/register",methods=["POST"])
def registration():
    datas = request.get_json()
    user = User(username = datas["username"])
    user.set_pass(datas["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message":"User Created Successfully!"}), 201

@auth_blues.route("/login", methods=["POST"])
def login():
    datas = request.get_json()
    user = User.query.filter_by(username=datas["username"]).first()
    if user and user.check_pass(datas["password"]):
        tokens = create_access_token(identity=user.id)
        return jsonify(access_token=tokens), 200
    return jsonify({"error":"Invalid! Please Try Again!"}), 401