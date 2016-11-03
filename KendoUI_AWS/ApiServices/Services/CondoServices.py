from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask import Blueprint
import traceback

import CondoInsertFunction
import CondoGetAllFunction
import CondoGetByIdFunction
import CondoUpdateFunction
import CondoDeleteFunction

condoApi = Blueprint("condoApi", __name__)

#Insertar un condominio nuevo
@condoApi.route('/api/condo', methods=['POST'])
def InsertNewCondo():

    db = CondoInsertFunction

    try:

        if not request.json or not 'Description' in request.json:
            abort(400)

        event = {
            'Description' : request.json['Description'],
            'Logo' : request.json['Logo'],
            'Url' : request.json['Url']
            }

        response = db.InsertNewCondo(event, "")

    except Exception:
        print("Error - Metodo InsertNewCondo")
        traceback.print_exc()
        return jsonify({"Resultado": "No se ha podido completar la transaccion"}), 201

    else:
        return jsonify({"Resultado" : "Datos ingresados correctamente"}), 201

#Obtener todos los condominios
@condoApi.route('/api/condo', methods=['GET'])
def GetAllCondos():

    db = CondoGetAllFunction

    try:

        response = db.GetAllCondos("", "")

    except Exception:
        print("Error - Metodo GetAllCondos")
        traceback.print_exc()
        return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

    return jsonify(response)

#Obtener un condominio por Id
@condoApi.route('/api/condo/<string:id>', methods=['GET'])
def GetById(id):

    db = CondoGetByIdFunction

    try:

        event = { "Id" : id }
        response = db.GetCondoById(event, "")

    except Exception:
        print("Error - Metodo GetById")
        traceback.print_exc()
        return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

    return jsonify(response)

#Actualizar un usuario
@condoApi.route('/api/condo/<string:id>', methods=['PUT'])
def UpdateCondo(id):

    db = CondoUpdateFunction

    try:

        if not request.json:
            abort(400)

        event = {
            'Id': id,
            'Description' : request.json['Description'],
            'Logo' : request.json['Logo'],
            'Url' : request.json['Url'],
            }

        response = db.UpdateCondo(event, "")

    except Exception:
        print("Error - Metodo UpdateCondo")
        traceback.print_exc()
        return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

    else:
        return jsonify(response), 201

#Eliminar un condominio
@condoApi.route('/api/condo/<string:id>', methods=['DELETE'])
def DeleteCondo(id):

    db = CondoDeleteFunction

    try:
        event = {"Id" : id}
        response = db.DeleteCondoById(event, "")

    except Exception:
        print("Error - Metodo DeleteCondo")
        traceback.print_exc()
        return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

    else:
        return jsonify({"Resultado" : "Condominio eliminado correctamente"}), 201
