
document.getElementById("boton-inicioCamara").addEventListener('click', function () {
    document.body.classList.add('slide-out-left');
    setTimeout(function () {
        window.location.href = '/inicioCamara';
    }
        , 200); // Duración de la animación en milisegundos
});
