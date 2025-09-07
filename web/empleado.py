from flask import render_template, request, jsonify, Blueprint

empleado = Blueprint('empleado', __name__)

@empleado.route('/')
def empleado_inicio():
    return render_template('/empleado/inicio-empleado.html')

@empleado.route('/registro')
def empleado_registro():
    return render_template('/empleado/anadir_registro.html')

