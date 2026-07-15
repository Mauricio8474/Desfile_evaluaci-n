# Evaluación "Hilos de la Tierra" - USM

Aplicación web para que los jurados evalúen el proyecto "Hilos de la Tierra" del programa de Diseño de Moda de la Institución Universitaria de Santa Marta (USM).

## Requisitos

- Python 3.10+
- pip

## Instalación

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
├── app.py              # Aplicación Flask (rutas, lógica)
├── config.py           # Configuración (DB, secret key)
├── models.py           # Modelos SQLAlchemy
├── seed_data.py        # Script de datos de prueba
├── requirements.txt    # Dependencias
├── templates/          # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── estudiantes.html
│   ├── calificar.html
│   └── reporte.html
├── static/
│   ├── css/style.css
│   └── js/main.js
└── instance/
    └── desfile.db      # Base de datos SQLite (auto-generada)
```

## Funcionalidades

- **Calificación**: Formulario con 11 criterios agrupados en 3 componentes (Portafolio 30%, Sustentación 30%, Runway 40%)
- **Cálculo automático**: Nota ponderada por componente y nota final con redondeo a 2 decimales
- **Reporte Excel**: Descarga en .xlsx con notas finales y detalle por jurado
- **Autenticación**: Login simple para jurados
- **API REST**: Endpoints para consultar estudiantes y calificaciones

## Uso

1. Abrir `http://127.0.0.1:5000`
2. Ingresar como jurado (sin contraseña)
3. Seleccionar estudiante y calificar cada criterio (0.0 - 5.0)
4. Ver reporte y descargar Excel

## Datos de prueba

- **10 estudiantes** (grupos A y B)
- **2 jurados**
- **11 criterios** de evaluación precargados

## Tecnologías

- Backend: Python + Flask + SQLAlchemy
- Frontend: Bootstrap 5 + CSS personalizado
- Base de datos: SQLite
- Exportación: openpyxl
