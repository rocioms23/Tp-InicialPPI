
    const botonToken = document.getElementById('boton-inicioToken');
    const ventanaToken= document.getElementById('tokenGenerado');
    const botonCerrar= document.getElementById('cerrarToken');
    botonToken.addEventListener('click', function () {
        ventanaToken.showModal();
        });
    botonCerrar.addEventListener('click', function () {
        ventanaToken.close();
        });
