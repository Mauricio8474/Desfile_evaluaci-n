# Manual de Usuario — Evaluaci&oacute;n "Hilos de la Tierra"

## Programa de Dise&ntilde;o de Moda — USM

---

## 1. Acceso al sistema

1. Abre tu navegador (Chrome, Firefox o Edge).
2. Ve a la direcci&oacute;n donde est&aacute; alojada la aplicaci&oacute;n: `http://127.0.0.1:5000` (local) o la URL que te haya proporcionado el administrador.
3. Ver&aacute;s la p&aacute;gina principal con tres opciones: **Estudiantes**, **Calificar** y **Reporte**.

## 2. Inicio de sesi&oacute;n

La aplicaci&oacute;n tiene dos tipos de ingreso:

### Para jurados
1. Haz clic en **Ingresar** en la barra de navegaci&oacute;n superior.
2. En la pesta&ntilde;a **Jurado**, selecciona tu nombre de la lista.
3. Si el administrador te asign&oacute; una contrase&ntilde;a, escr&iacute;bela. Si no, deja el campo vac&iacute;o.
4. Haz clic en **Ingresar como Jurado**.

### Para administradores
1. Haz clic en **Ingresar**.
2. En la pesta&ntilde;a **Administrador**, ingresa:
   - Usuario: `admin`
   - Contrase&ntilde;a: `admin123`
3. Haz clic en **Ingresar como Administrador**.

## 3. Ver listado de estudiantes

1. En la p&aacute;gina principal o en la barra de navegaci&oacute;n, haz clic en **Estudiantes**.
2. Ver&aacute;s el listado completo de estudiantes con c&oacute;digo y nombre.
3. Si has iniciado sesi&oacute;n como jurado, ver&aacute;s un bot&oacute;n **Calificar** junto a cada estudiante.

## 4. Calificar a un estudiante

Cada estudiante recibe su propia calificaci&oacute;n individual.

1. Aseg&uacute;rate de haber iniciado sesi&oacute;n como jurado.
2. Desde la p&aacute;gina principal, en la tarjeta **Calificar**, haz clic en **Seleccionar estudiante** y elige un estudiante.
3. Tambi&eacute;n puedes ir a **Estudiantes** y hacer clic en **Calificar** junto al estudiante deseado.
4. Se mostrar&aacute; un formulario con los 11 criterios de evaluaci&oacute;n agrupados en tres componentes:
   - **Portafolio de Dise&ntilde;o** (3 criterios, peso 30%)
   - **Sustentaci&oacute;n Oral** (4 criterios, peso 30%)
   - **Desarrollo de procesos y desempe&ntilde;o en el Runway** (4 criterios, peso 40%)
5. Ingresa una nota num&eacute;rica de **0.0 a 5.0** para cada criterio (puedes usar un decimal, ej. 4.5).
6. Observa la **barra de progreso** que muestra cu&aacute;ntos criterios has calificado.
7. Al terminar, haz clic en **Guardar calificaci&oacute;n**.
8. Recibir&aacute;s un mensaje de confirmaci&oacute;n. Puedes volver a calificar en cualquier momento; las notas anteriores se mostrar&aacute;n precargadas.

## 5. Panel de Administraci&oacute;n

Disponible solo para administradores. Desde el panel puedes:

### Gestionar estudiantes
- Crear, editar y eliminar estudiantes

### Cargar estudiantes desde Excel
1. En la secci&oacute;n **Estudiantes** del panel, haz clic en **Cargar Excel**.
2. Selecciona un archivo Excel con las columnas: **C&oacute;digo**, **Nombre**.
3. Si un c&oacute;digo ya existe, sus datos se actualizar&aacute;n.

### Gestionar jurados
- Crear, editar y eliminar jurados
- Asignar o cambiar contrase&ntilde;a

## 6. Ver reporte de calificaciones

1. En la barra de navegaci&oacute;n, haz clic en **Reporte**.
2. Se mostrar&aacute; una tabla con todos los estudiantes y sus notas calculadas:
   - **Nota Portafolio** (promedio ponderado de los criterios de Portafolio)
   - **Nota Sustentaci&oacute;n** (promedio ponderado de los criterios de Sustentaci&oacute;n)
   - **Nota Runway** (promedio ponderado de los criterios de Runway)
   - **Nota Final** (suma ponderada: 30% Portafolio + 30% Sustentaci&oacute;n + 40% Runway)
3. Si hay m&aacute;s de un jurado, se muestra el promedio y el **desglose por jurado** debajo de cada estudiante (para auditor&iacute;a).

## 7. Descargar reporte en Excel

1. En la p&aacute;gina de **Reporte**, haz clic en el bot&oacute;n **Descargar Excel**.
2. Se descargar&aacute; un archivo `.xlsx` con dos hojas:
   - **Hoja 1 — Notas finales**: Estudiante, c&oacute;digo, notas por componente y nota final.
   - **Hoja 2 — Detalle por jurado**: Todas las calificaciones individuales por criterio y jurado (para auditor&iacute;a).

## 8. Borrar todas las calificaciones (solo admin)

1. En la p&aacute;gina de **Reporte**, el administrador ve un bot&oacute;n **Borrar todas**.
2. Al hacer clic, aparece una confirmaci&oacute;n. Al aceptar, se eliminan todas las calificaciones de todos los jurados.
3. Esta acci&oacute;n **no se puede deshacer**.

## 9. Cerrar sesi&oacute;n

1. Haz clic en tu nombre en la barra de navegaci&oacute;n superior.
2. Selecciona **Cerrar sesi&oacute;n**.

## 10. Consejos &uacute;tiles

- Las notas deben estar entre **0.0 y 5.0**. El sistema valida este rango autom&aacute;ticamente.
- Todos los campos deben estar diligenciados para poder guardar.
- Puedes calificar parcialmente y volver despu&eacute;s: las notas guardadas se conservan.
- Si cometes un error, simplemente vuelve a calificar al estudiante y las notas anteriores se sobrescribir&aacute;n.
- Cada jurado tiene sus propias calificaciones, visibles en el desglose del reporte.
- El reporte en Excel puede abrirse con Microsoft Excel, LibreOffice Calc o Google Sheets.

---

*Documentaci&oacute;n v2.0 — Sistema de Evaluaci&oacute;n "Hilos de la Tierra"*
*Instituci&oacute;n Universitaria de Santa Marta — Programa de Dise&ntilde;o de Moda*
