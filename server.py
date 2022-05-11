
from flask import Flask, render_template, request
from app.controllers import respuesta, respuesta2
from config import Config


app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)
@app.route('/')
def inicio():
    return render_template("index.html")


# devuelve los datos con parametros predeterminados
@app.route('/datos', methods=['GET'])
def getDatos():
    al = respuesta()
    return al


@app.route('/datos2', methods=['GET'])
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

if __name__ == "__main__":
    app.run()  # No añadir parámetros, modificar directamente en Config
