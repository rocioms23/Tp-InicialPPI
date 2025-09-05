from flask import render_template, request, jsonify, Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/')
def admin_inicio():
    return render_template('/admin/inicio-admin.html')

@admin.route('/estadisticas')
def estadisticas():
    return render_template('/admin/estadistica-admin.html')

@admin.route('/actividad')
def actividad_empleados():
    return render_template('/admin/actividad-admin.html')
