document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById("videoSlither");
    const imagen = document.getElementById("imagenSlither");

    if (video && imagen) {
        video.addEventListener("error", function () {
            video.style.display = "none";
            imagen.style.display = "block";
        });
    }

    const boton = document.getElementById("theme-toggle");
    if (boton) {
        boton.addEventListener("click", function () {
            document.body.classList.toggle("light-mode");

            if (document.body.classList.contains("light-mode")) {
                boton.textContent = "🌙";
            } else {
                boton.textContent = "☀️";
            }
        });
    }
});