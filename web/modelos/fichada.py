from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fichada(db.Model):
    __tablename__ = 'fichada'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    imagen = db.Column(db.Text, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    decision = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Fichada {self.id}>'