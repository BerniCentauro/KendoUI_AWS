from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask import Blueprint
import traceback

import UserInsertFunction
import UserGetAllFunction
import UserGetByIdFunction
import UserUpdateFunction
import UserDeleteFunction

userApi = Blueprint("userApi", __name__)

#Insertar un usuario nuevo
@userApi.route('/api/user', methods=['POST'])
def InsertNewUser():

    db = UserInsertFunction

    try:

        if not request.json or not 'Username' in request.json:
            abort(400)

        event = {
            'Email' : request.json['Email'],
            'Password' : request.json['Password'],
            'Username' : request.json['Username'],
            'Phone' : request.json['Phone'],
            'Identification' : request.json['Identification']
            }

        response = db.InsertNewUser(event, "")

    except Exception:
        print("Error - Metodo InsertNewUser")
        traceback.print_exc()
        return jsonify({"Resultado": "No se ha podido completar la transaccion"}), 201

    else:
        return jsonify({"Resultado" : "Datos ingresados correctamente"}), 201

#Obtener todos los usuarios
@userApi.route('/api/user', methods=['GET'])
def GetAllUsers():

    db = UserGetAllFunction

    try:

        response = db.GetAllUsers("", "")

    except Exception:
        print("Error - Metodo GetAllUsers")
        traceback.print_exc()
        return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

    return jsonify(response)

#Obtener un usuario por Id
@userApi.route('/api/user/<string:id>', methods=['GET'])
def GetById(id):

    db = UserGetByIdFunction

    try:

        event = { "Id" : id }
        response = db.GetUserById(event, "")

    except Exception:
        print("Error - Metodo GetById")
        traceback.print_exc()
        return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

    return jsonify(response)

#Actualizar un usuario
@userApi.route('/api/user/<string:id>', methods=['PUT'])
def UpdateUser(id):

    db = UserUpdateFunction

    try:

        if not request.json:
            abort(400)

        event = {
            'Id': id,
            'Email' : request.json['Email'],
            'Password' : request.json['Password'],
            'Username' : request.json['Username'],
            'Phone' : request.json['Phone'],
            'Identification' : request.json['Identification']
            }

        response = db.UpdateUser(event, "")

    except Exception:
        print("Error - Metodo UpdateUser")
        traceback.print_exc()
        return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

    else:
        return jsonify(response), 201

#Eliminar un usuario
@userApi.route('/api/user/<string:id>', methods=['DELETE'])
def DeleteUser(id):

    db = UserDeleteFunction

    try:
        event = {"Id" : id}
        response = db.DeleteUserById(event, "")

    except Exception:
        print("Error - Metodo DeleteUser")
        traceback.print_exc()
        return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

    else:
        return jsonify({"Resultado" : "Usuario eliminado correctamente"}), 201

        