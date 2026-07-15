from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timezone

db = SQLAlchemy()

class Admin(UserMixin, db.Model):
    __tablename__ = 'administradores'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    nombre = db.Column(db.String(200), nullable=False)

    def get_id(self):
        return f'a_{self.id}'

    def __repr__(self):
        return f'<Admin {self.username}>'

class Grupo(db.Model):
    __tablename__ = 'grupos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.String(300), nullable=True)
    estudiantes = db.relationship('Estudiante', backref='grupo_obj', lazy=True)

    def __repr__(self):
        return f'<Grupo {self.nombre}>'

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupos.id'), nullable=True)
    grupo = db.Column(db.String(50), nullable=True)
    calificaciones = db.relationship('Calificacion', backref='estudiante', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Estudiante {self.nombre}>'

class Jurado(UserMixin, db.Model):
    __tablename__ = 'jurados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(200), nullable=True)
    calificaciones = db.relationship('Calificacion', backref='jurado', lazy=True, cascade='all, delete-orphan')

    def get_id(self):
        return f'j_{self.id}'

    def __repr__(self):
        return f'<Jurado {self.nombre}>'

class Criterio(db.Model):
    __tablename__ = 'criterios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)
    componente = db.Column(db.String(50), nullable=False)
    porcentaje = db.Column(db.Float, nullable=False)
    orden = db.Column(db.Integer, nullable=False, default=0)
    calificaciones = db.relationship('Calificacion', backref='criterio', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Criterio {self.nombre}>'

class Calificacion(db.Model):
    __tablename__ = 'calificaciones'
    id = db.Column(db.Integer, primary_key=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'), nullable=False)
    criterio_id = db.Column(db.Integer, db.ForeignKey('criterios.id'), nullable=False)
    jurado_id = db.Column(db.Integer, db.ForeignKey('jurados.id'), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (db.UniqueConstraint('estudiante_id', 'criterio_id', 'jurado_id', name='uq_est_crit_jurado'),)

    def __repr__(self):
        return f'<Calificacion {self.estudiante_id}/{self.criterio_id}/{self.jurado_id}: {self.nota}>'
