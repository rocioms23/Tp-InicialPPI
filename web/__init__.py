from flask import Flask

def crear_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Labo2025'
    from .rutas import registrar_rutas, vistas
    from .empleado import empleado
    from .admin import admin
    from .visualizar_dataset import generar_graficos
    from .cargarImagenes import generar_y_guardar_vectores
    app.register_blueprint(vistas, url_prefix='/')
    app.register_blueprint(empleado, url_prefix='/empleado')
    app.register_blueprint(admin, url_prefix='/admin')
    registrar_rutas(app)

    generar_graficos()
#    generar_y_guardar_vectores("web/data/db_rostros/")
    return app