from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
import traceback

from UserServices import userApi
from CondoServices import condoApi
from FincaFilialServices import ffApi

class MainServices:

    def runServices():

        #Instanciar flask
        app = Flask(__name__)

        #Instanciar servicios
        app.register_blueprint(userApi)
        app.register_blueprint(condoApi)
        app.register_blueprint(ffApi)

        #Ruta por default
        @app.route("/")
        def default():
            return "KendoUI_AWS Example"

        #Manejo de errores
        @app.errorhandler(404)
        def not_found(error):
            return make_response(jsonify({"Error": "Datos no encontrados"}), 404)

        #Correr el servidor
        if __name__ == "MainServices":
            app.run(debug=True)
