document.addEventListener('DOMContentLoaded', function() {
    var links = document.querySelectorAll('.nav-link');
    links.forEach(function(link) {
        link.addEventListener('click', function() {
            // Eliminar la clase 'active' de todos los enlaces
            links.forEach(function(link) {
                link.classList.remove('active');
            });
            // Agregar la clase 'active' al enlace clickeado
            link.classList.add('active');
        });
    });
});