import bcrypt
from app import app, db, init_db
from models import Admin, Estudiante, Jurado, Criterio, Calificacion

def seed():
    with app.app_context():
        init_db()

        if Admin.query.count() == 0:
            admin = Admin(
                username='admin',
                password=bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                nombre='Administrador USM'
            )
            db.session.add(admin)

        if Estudiante.query.count() == 0:
            estudiantes = [
                Estudiante(nombre='Ana Mar\u00eda Rodr\u00edguez', codigo='2021001'),
                Estudiante(nombre='Carlos Andr\u00e9s P\u00e9rez', codigo='2021002'),
                Estudiante(nombre='Laura Valentina Garc\u00eda', codigo='2021003'),
                Estudiante(nombre='Miguel \u00c1ngel Torres', codigo='2021004'),
                Estudiante(nombre='Sof\u00eda Carolina Mart\u00ednez', codigo='2021005'),
                Estudiante(nombre='Daniel Esteban L\u00f3pez', codigo='2021006'),
                Estudiante(nombre='Mar\u00eda Jos\u00e9 Castillo', codigo='2021007'),
                Estudiante(nombre='Juan Sebasti\u00e1n Ram\u00edrez', codigo='2021008'),
                Estudiante(nombre='Valentina Andrea Moreno', codigo='2021009'),
                Estudiante(nombre='Felipe Antonio Jim\u00e9nez', codigo='2021010'),
            ]
            db.session.add_all(estudiantes)

        if Jurado.query.count() == 0:
            jurados = [
                Jurado(nombre='Jurado 1 - Prof. Elena Vargas', email='elena.vargas@usm.edu.co'),
                Jurado(nombre='Jurado 2 - Prof. Roberto D\u00edaz', email='roberto.diaz@usm.edu.co'),
            ]
            db.session.add_all(jurados)

        db.session.commit()
        print('Datos de prueba insertados correctamente.')
        print(f'Administradores: {Admin.query.count()}')
        print(f'Estudiantes: {Estudiante.query.count()}')
        print(f'Jurados: {Jurado.query.count()}')
        print(f'Criterios: {Criterio.query.count()}')

if __name__ == '__main__':
    seed()
