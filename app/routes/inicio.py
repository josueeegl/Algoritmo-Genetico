from flask import Blueprint, render_template, jsonify, request
from ..controllers import respuesta, respuesta2

ini = Blueprint("views", __name__)


@ini.route('/')
def inicio():
    return render_template("index.html")


# devuelve los datos con parametros predeterminados
@ini.route('/datos', methods=['GET'])
def getDatos():
    al = respuesta()
    return al


@ini.route('/datos2', methods=['GET'])
def getDParams():
    convergencia = request.args.get('convergencia')
    target = request.args.get('target')
    nVacunas = request.args.get('nVacunas')
    nContagios = request.args.get('nContagios')
    nIndividuos = request.args.get('nIndividuos')
    rango = request.args.get('rango')
    max = request.args.get('max')
    min = request.args.get('min')

    al = respuesta2(convergencia, target, nVacunas,
                    nContagios, nIndividuos, rango, max, min)
    return al
