document.querySelector("#boton-verificar").addEventListener("click", async () => {
    let video = document.getElementById("camaraVideo");
    let canvas = document.getElementById("areaCamara");
    let ctx = canvas.getContext("2d");

    // Ajustar canvas al tamaño del video
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    // Dibujar frame actual
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convertir a Base64
    let dataURL = canvas.toDataURL("image/jpeg");

    // Enviar a Flask
    try {
        let response = await fetch("/verificar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ image: dataURL })
        });

        let data = await response.json();

        // Muestra el resultado de la verificación en la consola
        console.log("Respuesta del servidor:", data);

        // Aquí puedes usar la propiedad 'verified' si la devuelves desde Flask
        if (data.verified) {
            console.log("¡Rostro verificado!");
            window.location.href = '/empleado/';
        } else {
            console.log("Rostro no verificado.");
        }

    }
    catch (error) {
        console.error("Error al recibir la respuesta:", error);
    }

});