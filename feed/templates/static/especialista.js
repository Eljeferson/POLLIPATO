document.addEventListener('DOMContentLoaded', function() {
    var especialistas = document.querySelectorAll('.especialista-container');
    var index = 0;

    function showNextEspecialista() {
        especialistas.forEach(function(especialista) {
            especialista.style.display = 'none';
        });

        especialistas[index].style.display = 'block';
        index = (index + 1) % especialistas.length;
    }

    setInterval(showNextEspecialista, 10000);  // Cambiar cada 10 segundos
});





