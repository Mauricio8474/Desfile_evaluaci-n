import bcrypt
from app import app, db, init_db
from models import Estudiante, Jurado, Criterio, Calificacion

def seed():
    with app.app_context():
        init_db()
        if Estudiante.query.count() == 0:
            estudiantes = [
                Estudiante(nombre='Ana María Rodríguez', codigo='2021001', grupo='A'),
                Estudiante(nombre='Carlos Andrés Pérez', codigo='2021002', grupo='A'),
                Estudiante(nombre='Laura Valentina García', codigo='2021003', grupo='A'),
                Estudiante(nombre='Miguel Ángel Torres', codigo='2021004', grupo='B'),
                Estudiante(nombre='Sofía Carolina Martínez', codigo='2021005', grupo='B'),
                Estudiante(nombre='Daniel Esteban López', codigo='2021006', grupo='B'),
                Estudiante(nombre='María José Castillo', codigo='2021007', grupo='A'),
                Estudiante(nombre='Juan Sebastián Ramírez', codigo='2021008', grupo='A'),
                Estudiante(nombre='Valentina Andrea Moreno', codigo='2021009', grupo='B'),
                Estudiante(nombre='Felipe Antonio Jiménez', codigo='2021010', grupo='B'),
            ]
            db.session.add_all(estudiantes)
        if Jurado.query.count() == 0:
            jurados = [
                Jurado(nombre='Jurado 1 - Prof. Elena Vargas', email='elena.vargas@usm.edu.co'),
                Jurado(nombre='Jurado 2 - Prof. Roberto Díaz', email='roberto.diaz@usm.edu.co'),
            ]
            db.session.add_all(jurados)
        db.session.commit()
        print('Datos de prueba insertados correctamente.')
        print(f'Estudiantes: {Estudiante.query.count()}')
        print(f'Jurados: {Jurado.query.count()}')
        print(f'Criterios: {Criterio.query.count()}')

if __name__ == '__main__':
    seed()
