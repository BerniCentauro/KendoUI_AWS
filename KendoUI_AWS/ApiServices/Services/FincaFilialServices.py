from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
from flask_httpauth import HTTPBasicAuth
import traceback

import FincaFilialDeleteFunction
import FincaFilialGetAllFunction
import FincaFilialGetByIdFunction
import FincaFilialInsertFunction
import FincaFilialUpdateFunction
import FincaFilialGetAllFunction

class FincaFilialServices:

    def runServices():

        #Instanciar flask
        app = Flask(__name__)

        #Insertar una finca filial nueva
        @app.route('/api/fincaFilial', methods=['POST'])
        def InsertNewFincaFilial():

            db = FincaFilialInsertFunction

            try:

                if not request.json or not 'Id' in request.json:
                    abort(400)

                event = {
                    'Id': request.json['Id'],
                    'Status' : request.json['Status'],
                    'NumberProperty' : request.json['NumberProperty'],
                    'IdCondominio' : request.json['IdCondominio'],
                    'IdUser' : request.json['IdUser']
                    }

                response = db.InsertNewFincaFilial(event, "")

            except Exception:
                print("Error - Metodo InsertNewFincaFilial")
                traceback.print_exc()
                return jsonify({"Resultado": "No se ha podido completar la transaccion"}), 201

            else:
                return jsonify({"Resultado" : "Datos ingresados correctamente"}), 201

        #Obtener lista de finca Filial
        @app.route('/api/fincaFilial', methods=['GET'])
        def GetAllFincaFilial():

            db = FincaFilialGetAllFunction
            
            try:
                
                response = db.GetAllFincaFilial("", "")

            except Exception:
                print("Error - Metodo GetAllFincaFilial")
                traceback.print_exc()
                return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

            return jsonify({"FincaFilial" : response})

        #Obtener una finca filial por Id
        @app.route('/api/fincaFilial/<string:id>', methods=['GET'])
        def GetById(id):

            #db = GetFincaFilialById
            return jsonify({"FincaFilial" : "holi"})

            db = FincaFilialGetAllFunction

            try:

                event = { "Id" : id }
                response = db.GetFincaFilialById(event, "")

            except Exception:
                print("Error - Metodo GetById")
                traceback.print_exc()
                return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

            return jsonify({"FincaFilial" : response})

        #Actualizar una finca filial
        @app.route('/api/fincaFilial/<string:id>', methods=['PUT'])
        def UpdateFincaFilial(id):

            db = FincaFilialUpdateFunction

            try:

                if not request.json:
                    abort(400)

                event = {
                    'Id': request.json['Id'],
                    'Status' : request.json['Status'],
                    'NumberProperty' : request.json['NumberProperty'],
                    'IdCondominio' : request.json['IdCondominio'],
                    'IdUser' : request.json['IdUser']
                    }

                response = db.UpdateFincaFilial(event, "")

            except Exception:
                print("Error - Metodo actualizar finca Filial")
                traceback.print_exc()
                return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

            else:
                return jsonify({"FincaFilial": response}), 201

        #Eliminar una finca filial
        @app.route('/api/fincaFilial/<string:id>', methods=['DELETE'])
        def DeleteFincaFilial(id):

            db = FincaFilialDeleteFunction

            try:
                event = {"Id" : id}
                response = db.DeleteFincaFilialById(event, "")

            except Exception:
                print("Error - Metodo borrar finca filial")
                traceback.print_exc()
                return jsonify({"Error": "No se ha podido completar la transaccion"}), 201

            else:
                return jsonify({"Resultado" : "Finca filial eliminada correctamente"}), 201

        #Manejo de errores
        @app.errorhandler(404)
        def not_found(error):
            return make_response(jsonify({"Error": "Datos no encontrados"}), 404)

        #Correr el servidor
        if __name__ == "FincaFilialServices":
            app.run(debug=True)