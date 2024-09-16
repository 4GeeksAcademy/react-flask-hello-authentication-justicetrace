"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)
# Setup the Flask-JWT-Extended extension

# Allow CORS requests to this API
CORS(api)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route('/token', methods=['POST'])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("username", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@api.route('/hello', methods=['GET'])
@jwt_required()
def get_hello():

    user = get_jwt_identity()
    dictonary = {
         "message": "hello world" + user
    }
    return jsonify(dictonary)