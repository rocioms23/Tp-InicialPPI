from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Imagen(db.Model):
    __tablename__ = 'imagenes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=True)
    vector_imagen = db.Column(db.Text, nullable=True)
    ubicacion_archivo = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Imagen {self.id}>'
