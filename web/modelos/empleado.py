from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Empleado(db.Model):
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    legajo = db.Column(db.String(50), unique=True, nullable=False)
    id_imagen = db.Column(db.Integer, db.ForeignKey('imagenes.id'))
    fecha_ingreso = db.Column(db.Date)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    id_sector = db.Column(db.Integer, db.ForeignKey('sectores.id'))
    id_turno = db.Column(db.Integer, db.ForeignKey('turnos.id'))
    id_rol = db.Column(db.Integer, db.ForeignKey('puestos.id'))
    
    def __repr__(self):
        return f'<Empleado {self.legajo}>'