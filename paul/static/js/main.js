// Marca en el menú el enlace de la sección en la que estamos
document.querySelectorAll('.menu a').forEach(function (enlace) {
    var href = enlace.getAttribute('href');
    var ruta = window.location.pathname;
    if (ruta === href || (href !== '/' && ruta.startsWith(href))) {
        enlace.classList.add('activo');
    }
});
