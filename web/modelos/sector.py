from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sector(db.Model):
    __tablename__ = 'sectores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50))
    detalle = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return f'<Sector {self.nombre}>'
