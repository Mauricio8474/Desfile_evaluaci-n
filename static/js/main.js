document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('.nota-input');
    const barra = document.getElementById('barra-progreso');
    const progresoTexto = document.getElementById('progreso-texto');

    function actualizarProgreso() {
        let calificados = 0;
        const total = inputs.length;
        inputs.forEach(function(input) {
            const val = parseFloat(input.value);
            if (input.value !== '' && !isNaN(val) && val >= 0 && val <= 5) {
                calificados++;
                input.classList.remove('invalido');
                input.classList.add('valido');
            } else if (input.value !== '') {
                input.classList.add('invalido');
                input.classList.remove('valido');
            } else {
                input.classList.remove('valido', 'invalido');
            }
        });
        if (barra) {
            const pct = total > 0 ? Math.round((calificados / total) * 100) : 0;
            barra.style.width = pct + '%';
        }
        if (progresoTexto) {
            progresoTexto.textContent = calificados + '/' + total;
        }
    }

    inputs.forEach(function(input) {
        input.addEventListener('input', actualizarProgreso);
        actualizarProgreso();
    });

    const formCalif = document.getElementById('form-calificacion');
    if (formCalif) {
        formCalif.addEventListener('submit', function(e) {
            let valid = true;
            inputs.forEach(function(input) {
                const val = parseFloat(input.value);
                if (input.value === '' || isNaN(val) || val < 0 || val > 5) {
                    valid = false;
                    input.classList.add('invalido');
                }
            });
            if (!valid) {
                e.preventDefault();
                alert('Por favor, verifica que todas las notas estén en el rango de 0.0 a 5.0.');
            }
        });
    }

    const alertas = document.querySelectorAll('.alert-dismissible');
    alertas.forEach(function(alert) {
        setTimeout(function() {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});
