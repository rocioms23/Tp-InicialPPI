from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Puesto(db.Model):
    __tablename__ = 'Puestos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=True)
    descripcion = db.Column(db.Text, nullable=True)
    rol = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Puesto {self.nombre}>'