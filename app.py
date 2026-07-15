import os
import bcrypt
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Estudiante, Jurado, Criterio, Calificacion
from config import Config
from datetime import datetime, timezone
from io import BytesIO
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor inicia sesión para acceder.'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Jurado, int(user_id))

def init_db():
    with app.app_context():
        db.create_all()
        if Criterio.query.count() == 0:
            criterios = [
                Criterio(nombre='Investigación y concepto', componente='Portafolio', porcentaje=10, orden=1),
                Criterio(nombre='Ilustraciones: Figurines', componente='Portafolio', porcentaje=10, orden=2),
                Criterio(nombre='Fichas Técnicas', componente='Portafolio', porcentaje=10, orden=3),
                Criterio(nombre='Vocabulario técnico y seguridad', componente='Sustentación', porcentaje=10, orden=4),
                Criterio(nombre='Presentación y Estética', componente='Sustentación', porcentaje=10, orden=5),
                Criterio(nombre='Presentación Personal', componente='Sustentación', porcentaje=5, orden=6),
                Criterio(nombre='Lookbook o Vídeo', componente='Sustentación', porcentaje=5, orden=7),
                Criterio(nombre='Precisión y claridad técnica en el patrón', componente='Runway', porcentaje=10, orden=8),
                Criterio(nombre='Materialización: intervención textil y estructura', componente='Runway', porcentaje=10, orden=9),
                Criterio(nombre='Estilismo y Coherencia Visual "Total Look"', componente='Runway', porcentaje=10, orden=10),
                Criterio(nombre='Desempeño en Backstage y Disciplina', componente='Runway', porcentaje=10, orden=11),
            ]
            db.session.add_all(criterios)
            db.session.commit()

def calcular_notas(estudiante_id, jurado_id):
    calificaciones = Calificacion.query.filter_by(
        estudiante_id=estudiante_id, jurado_id=jurado_id
    ).all()
    if not calificaciones:
        return None
    calif_dict = {c.criterio_id: c.nota for c in calificaciones}
    componentes = {'Portafolio': 0.30, 'Sustentación': 0.30, 'Runway': 0.40}
    notas_componente = {}
    for comp, peso_global in componentes.items():
        criterios = Criterio.query.filter_by(componente=comp).order_by(Criterio.orden).all()
        suma_ponderada = 0
        suma_porcentajes = 0
        for c in criterios:
            if c.id in calif_dict:
                suma_ponderada += calif_dict[c.id] * c.porcentaje
                suma_porcentajes += c.porcentaje
        if suma_porcentajes > 0:
            notas_componente[comp] = round(suma_ponderada / suma_porcentajes, 2)
        else:
            notas_componente[comp] = 0
    nota_final = round(
        notas_componente.get('Portafolio', 0) * 0.30 +
        notas_componente.get('Sustentación', 0) * 0.30 +
        notas_componente.get('Runway', 0) * 0.40,
        2
    )
    return {'notas_componente': notas_componente, 'nota_final': nota_final}

def calcular_promedio_jurados(estudiante_id):
    jurados = Jurado.query.all()
    notas_finales = []
    for j in jurados:
        resultado = calcular_notas(estudiante_id, j.id)
        if resultado:
            notas_finales.append({'jurado': j, 'resultado': resultado})
    if not notas_finales:
        return None
    prom_portafolio = round(sum(nf['resultado']['notas_componente'].get('Portafolio', 0) for nf in notas_finales) / len(notas_finales), 2)
    prom_sustentacion = round(sum(nf['resultado']['notas_componente'].get('Sustentación', 0) for nf in notas_finales) / len(notas_finales), 2)
    prom_runway = round(sum(nf['resultado']['notas_componente'].get('Runway', 0) for nf in notas_finales) / len(notas_finales), 2)
    prom_final = round(
        prom_portafolio * 0.30 + prom_sustentacion * 0.30 + prom_runway * 0.40,
        2
    )
    return {
        'notas_finales': notas_finales,
        'promedio_portafolio': prom_portafolio,
        'promedio_sustentacion': prom_sustentacion,
        'promedio_runway': prom_runway,
        'promedio_final': prom_final
    }

@app.route('/')
def index():
    estudiantes = Estudiante.query.order_by(Estudiante.nombre).all()
    jurados = Jurado.query.order_by(Jurado.nombre).all()
    return render_template('index.html', estudiantes=estudiantes, jurados=jurados)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        jurado_id = request.form.get('jurado_id')
        password = request.form.get('password')
        jurado = db.session.get(Jurado, int(jurado_id)) if jurado_id and jurado_id.isdigit() else None
        if jurado and jurado.password:
            if bcrypt.checkpw(password.encode('utf-8'), jurado.password.encode('utf-8')):
                login_user(jurado)
                flash(f'Bienvenido/a {jurado.nombre}', 'success')
                return redirect(url_for('index'))
            else:
                flash('Contraseña incorrecta', 'error')
        elif jurado and not jurado.password:
            login_user(jurado)
            flash(f'Bienvenido/a {jurado.nombre}', 'success')
            return redirect(url_for('index'))
        else:
            flash('Jurado no encontrado', 'error')
    jurados = Jurado.query.order_by(Jurado.nombre).all()
    return render_template('login.html', jurados=jurados)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('login'))

@app.route('/estudiantes')
def listar_estudiantes():
    estudiantes = Estudiante.query.order_by(Estudiante.grupo, Estudiante.nombre).all()
    return render_template('estudiantes.html', estudiantes=estudiantes)

@app.route('/calificar/<int:estudiante_id>', methods=['GET', 'POST'])
@login_required
def calificar(estudiante_id):
    estudiante = db.session.get(Estudiante, estudiante_id)
    if not estudiante:
        flash('Estudiante no encontrado', 'error')
        return redirect(url_for('index'))
    criterios = Criterio.query.order_by(Criterio.orden).all()
    if request.method == 'POST':
        todas_validas = True
        for c in criterios:
            nota_key = f'nota_{c.id}'
            if nota_key in request.form and request.form[nota_key].strip() != '':
                try:
                    nota = float(request.form[nota_key])
                    if nota < 0 or nota > 5:
                        flash(f'La nota para "{c.nombre}" debe estar entre 0.0 y 5.0', 'error')
                        todas_validas = False
                        continue
                    existing = Calificacion.query.filter_by(
                        estudiante_id=estudiante_id, criterio_id=c.id, jurado_id=current_user.id
                    ).first()
                    if existing:
                        existing.nota = nota
                        existing.fecha = datetime.now(timezone.utc)
                    else:
                        cal = Calificacion(
                            estudiante_id=estudiante_id, criterio_id=c.id,
                            jurado_id=current_user.id, nota=nota
                        )
                        db.session.add(cal)
                except ValueError:
                    flash(f'Valor inválido para "{c.nombre}"', 'error')
                    todas_validas = False
            else:
                flash(f'Debes calificar "{c.nombre}"', 'error')
                todas_validas = False
        if todas_validas:
            db.session.commit()
            flash(f'Calificaciones guardadas para {estudiante.nombre}', 'success')
            return redirect(url_for('index'))
        db.session.rollback()
    calificaciones_existentes = Calificacion.query.filter_by(
        estudiante_id=estudiante_id, jurado_id=current_user.id
    ).all()
    calif_dict = {c.criterio_id: c.nota for c in calificaciones_existentes}
    criterios_por_componente = {}
    for c in criterios:
        criterios_por_componente.setdefault(c.componente, []).append(c)
    componentes_orden = {'Portafolio': 0, 'Sustentación': 1, 'Runway': 2}
    criterios_por_componente = dict(
        sorted(criterios_por_componente.items(), key=lambda x: componentes_orden.get(x[0], 99))
    )
    return render_template('calificar.html', estudiante=estudiante, criterios_por_componente=criterios_por_componente, calif_dict=calif_dict, total_criterios=len(criterios))

@app.route('/reporte')
def reporte():
    estudiantes = Estudiante.query.order_by(Estudiante.nombre).all()
    jurados = Jurado.query.order_by(Jurado.nombre).all()
    datos = []
    for e in estudiantes:
        resultado = calcular_promedio_jurados(e.id)
        if resultado:
            datos.append({'estudiante': e, 'resultado': resultado})
    return render_template('reporte.html', datos=datos, jurados=jurados)

@app.route('/exportar_excel')
def exportar_excel():
    wb = openpyxl.Workbook()
    header_font = Font(bold=True, color='FFFFFF', size=11)
    header_fill = PatternFill(start_color='0033A0', end_color='0033A0', fill_type='solid')
    header_alignment = Alignment(horizontal='center', vertical='center')
    thin_border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )

    ws1 = wb.active
    ws1.title = 'Notas finales'
    headers1 = ['Estudiante', 'Código', 'Grupo', 'Nota Portafolio', 'Nota Sustentación', 'Nota Runway', 'Nota Final']
    for col, h in enumerate(headers1, 1):
        cell = ws1.cell(row=1, column=col, value=h)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment
        cell.border = thin_border

    estudiantes = Estudiante.query.order_by(Estudiante.nombre).all()
    row = 2
    for e in estudiantes:
        resultado = calcular_promedio_jurados(e.id)
        ws1.cell(row=row, column=1, value=e.nombre).border = thin_border
        ws1.cell(row=row, column=2, value=e.codigo).border = thin_border
        ws1.cell(row=row, column=3, value=e.grupo or '').border = thin_border
        if resultado:
            ws1.cell(row=row, column=4, value=resultado['promedio_portafolio']).border = thin_border
            ws1.cell(row=row, column=5, value=resultado['promedio_sustentacion']).border = thin_border
            ws1.cell(row=row, column=6, value=resultado['promedio_runway']).border = thin_border
            ws1.cell(row=row, column=7, value=resultado['promedio_final']).border = thin_border
        else:
            for col in range(4, 8):
                ws1.cell(row=row, column=col, value='Sin notas').border = thin_border
        row += 1

    for col in range(1, 8):
        ws1.column_dimensions[chr(64 + col)].width = 22

    ws2 = wb.create_sheet('Detalle por jurado')
    headers2 = ['Estudiante', 'Jurado', 'Criterio', 'Componente', 'Nota']
    for col, h in enumerate(headers2, 1):
        cell = ws2.cell(row=1, column=col, value=h)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment
        cell.border = thin_border

    calificaciones = Calificacion.query.order_by(Calificacion.estudiante_id, Calificacion.jurado_id, Calificacion.criterio_id).all()
    row = 2
    for cal in calificaciones:
        ws2.cell(row=row, column=1, value=cal.estudiante.nombre).border = thin_border
        ws2.cell(row=row, column=2, value=cal.jurado.nombre).border = thin_border
        ws2.cell(row=row, column=3, value=cal.criterio.nombre).border = thin_border
        ws2.cell(row=row, column=4, value=cal.criterio.componente).border = thin_border
        ws2.cell(row=row, column=5, value=cal.nota).border = thin_border
        row += 1

    for col in range(1, 6):
        ws2.column_dimensions[chr(64 + col)].width = 28

    output = BytesIO()
    wb.save(output)
    output.seek(0)
    return send_file(output, download_name='evaluacion_hilos_de_la_tierra.xlsx', as_attachment=True, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.route('/api/estudiantes')
def api_estudiantes():
    estudiantes = Estudiante.query.order_by(Estudiante.nombre).all()
    return jsonify([{'id': e.id, 'nombre': e.nombre, 'codigo': e.codigo, 'grupo': e.grupo} for e in estudiantes])

@app.route('/api/calificacion/<int:estudiante_id>/<int:jurado_id>')
def api_calificacion(estudiante_id, jurado_id):
    resultado = calcular_notas(estudiante_id, jurado_id)
    return jsonify(resultado)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
