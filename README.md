# Evaluaci&oacute;n "Hilos de la Tierra" - USM

Aplicaci&oacute;n web para que los jurados eval&uacute;en el proyecto "Hilos de la Tierra" del programa de Dise&ntilde;o de Moda de la Instituci&oacute;n Universitaria de Santa Marta (USM).

## Requisitos

- Python 3.10+
- pip

## Instalaci&oacute;n

```bash
git clone <repo-url>
cd desfile_evaluacion
pip install -r requirements.txt
python seed_data.py    # Precarga datos de prueba
python app.py          # Inicia el servidor
```

Abrir en el navegador: `http://127.0.0.1:5000`

## Estructura del proyecto

```
desfile_evaluacion/
├── app.py                  # Aplicaci&oacute;n Flask (rutas, l&oacute;gica)
├── config.py               # Configuraci&oacute;n (DB, secret key)
├── models.py               # Modelos SQLAlchemy (Admin, Grupo, Estudiante, Jurado, Criterio, Calificacion)
├── seed_data.py            # Script de datos de prueba
├── requirements.txt        # Dependencias
├── templates/              # Plantillas HTML
│   ├── base.html           # Layout principal
│   ├── index.html          # P&aacute;gina de inicio
│   ├── login.html          # Login (jurado y administrador)
│   ├── estudiantes.html    # Listado de estudiantes por grupo
│   ├── calificar.html      # Formulario de calificaci&oacute;n individual
│   ├── reporte.html        # Reporte de calificaciones
│   └── admin/              # Panel de administraci&oacute;n
│       ├── index.html
│       ├── grupos.html
│       ├── grupo_form.html
│       ├── estudiantes.html
│       ├── estudiante_form.html
│       ├── estudiantes_cargar.html
│       ├── jurados.html
│       └── jurado_form.html
├── static/
│   ├── css/style.css
│   └── js/main.js
└── instance/
    └── desfile.db           # Base de datos SQLite (auto-generada)
```

## Funcionalidades

- **Calificaci&oacute;n individual**: Formulario con 11 criterios (Portafolio 30%, Sustentaci&oacute;n 30%, Runway 40%) por cada estudiante.
- **C&aacute;lculo autom&aacute;tico**: Nota ponderada por componente y nota final con redondeo a 2 decimales.
- **M&uacute;ltiples jurados**: Cada jurado califica independientemente. El reporte muestra promedio y desglose por jurado.
- **Reporte Excel**: Descarga en .xlsx con notas finales y detalle por jurado (para auditor&iacute;a).
- **Autenticaci&oacute;n**: Login para jurados (sin contrase&ntilde;a opcional) y administradores.
- **Panel de Administraci&oacute;n**: CRUD completo de grupos, estudiantes y jurados.
- **Carga masiva**: Importar estudiantes desde Excel con creaci&oacute;n autom&aacute;tica de grupos.
- **Horarios de sustentaci&oacute;n**: Cada grupo tiene un horario configurable.
- **API REST**: Endpoints para consultar estudiantes y calificaciones.

## Uso

### Para jurados
1. Abrir `http://127.0.0.1:5000`
2. Ingresar como jurado (seleccionar nombre, contrase&ntilde;a opcional)
3. En "Calificar", seleccionar un estudiante
4. Ingresar notas (0.0 - 5.0) en los 11 criterios
5. Ver reporte y descargar Excel

### Para administradores
1. Ingresar con usuario: `admin`, contrase&ntilde;a: `admin123`
2. Panel de Administraci&oacute;n para gestionar grupos, estudiantes y jurados
3. Opci&oacute;n "Cargar Excel" para importar estudiantes masivamente

## Datos de prueba (seed)

- **1 administrador**: admin / admin123
- **2 grupos**: Grupo A (Lunes 8:00 AM), Grupo B (Lunes 10:00 AM)
- **10 estudiantes** distribuidos en los grupos
- **2 jurados**
- **11 criterios** de evaluaci&oacute;n precargados

## Tecnolog&iacute;as

- Backend: Python + Flask + SQLAlchemy + Flask-Login
- Frontend: Bootstrap 5 + CSS personalizado (colores USM #0033A0 y tonos tierra)
- Base de datos: SQLite
- Exportaci&oacute;n: openpyxl
- Autenticaci&oacute;n: bcrypt

## Despliegue en Render (gratis)

1. Sube el repo a GitHub
2. Crea cuenta en https://render.com
3. New + Web Service → conecta tu repo
4. Render detecta Python/Flask autom&aacute;ticamente
5. Start Command: `gunicorn app:app`
6. Listo, URL: `https://tu-app.onrender.com`

## Ramas

- `main` — Producci&oacute;n
- `develop` — Desarrollo activo
- `test` — Pruebas
