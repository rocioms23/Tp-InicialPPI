from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def crear_app():
    app = Flask(__name__)
    app.secret_key = 'Labo2025'

    from .rutas import vistas
    from .empleado import empleado
    from .admin import admin

    from .cargarImagenes import generar_y_guardar_vectores
    #generar_y_guardar_vectores("web/data/db_rostros/")
    app.register_blueprint(vistas, url_prefix='/')
    app.register_blueprint(empleado, url_prefix='/empleado')
    app.register_blueprint(admin, url_prefix='/admin')

    return app