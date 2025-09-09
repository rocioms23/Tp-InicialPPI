
document.querySelector(".formulario-login").addEventListener('submit', function(e) {
    e.preventDefault();
        const emailIngresado = document.getElementById('email').value;
        const contrasenaIngresado = document.getElementById('contrasena').value;

        verificarUsuario(emailIngresado, contrasenaIngresado)
});

async function verificarUsuario(email, contrasena){
    const mensajeError = document.getElementById('mensajeError');
 try {
        const response = await fetch('/verificarAdmin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({  // <--- Convertir el objeto a JSON
                'email': email,
                'contrasena': contrasena
            })
        });

        // La respuesta del servidor es un objeto JSON
        const data = await response.json();

        if (response.ok) {
            // Inicio de sesión exitoso (status 200)
            console.log("Inicio de sesión exitoso:", data.message);
            
            // Oculta el mensaje de error si estaba visible
            mensajeError.classList.add('hidden');

            document.body.classList.add('slide-out-left');
            setTimeout(function() {
                window.location.href = '/admin/';
            }, 500);

        } else {
            // Inicio de sesión fallido (status 401 o 500)
            console.error("Error en inicio de sesión:", data.message);
            // Muestra el mensaje de error
            mensajeError.classList.remove('hidden');
            document.getElementById('email').value = '';
            document.getElementById('contrasena').value = '';
        }
    } catch (error) {
        // En caso de error de red o de otro tipo
        console.error('Error de red o del servidor:', error);
        mensajeError.classList.remove('hidden');
    }    
}


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
