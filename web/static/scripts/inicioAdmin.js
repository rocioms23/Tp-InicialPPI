
document.querySelector(".formulario-login").addEventListener('submit', function(e) {
    e.preventDefault();
        const emailIngresado = document.getElementById('email').value;
        const contraseñaIngresado = document.getElementById('contrasena').value;

        if(verificarUsuarioRegistrado(emailIngresado, contraseñaIngresado)) {
            document.body.classList.add('slide-out-left');
            setTimeout(function() {
                window.location.href = '/admin/';
            }
            , 500); // Duración de la animación en milisegundos
        }
        else {
            document.getElementById('email').value = '';
            document.getElementById('contrasena').value = '';
        }
});

function verificarUsuarioRegistrado(email, constrasena) {

    // Simulación administrador registrado
    const adminRegistrados = [
        { email: 'admin@empresa.com', contrasena: '1234' },
    ];

    // Buscar usuario por nombre
    const adminRegistrado = adminRegistrados.find(usuario => usuario.email === email);

    if (!adminRegistrado) {
        const mensaje = document.getElementById('mensajeError');
        mensaje.classList.remove('hidden');
        return false;
    }

    if (adminRegistrado.contrasena !== constrasena) {
        const mensaje = document.getElementById('mensajeError');
        mensaje.classList.remove('hidden');
        return false;
    }

    // Usuario registrado y contraseña correcta
    return true;
}
