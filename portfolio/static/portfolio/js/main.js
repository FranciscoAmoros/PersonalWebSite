document.addEventListener("DOMContentLoaded", function () {
    // --- Video con imagen de respaldo ---
    const video = document.getElementById("videoSlither");
    const imagen = document.getElementById("imagenSlither");

    if (video && imagen) {
        video.addEventListener("error", function () {
            video.style.display = "none";
            imagen.style.display = "block";
        });
    }

    // --- Tema claro/oscuro (se guarda entre páginas) ---
    const boton = document.getElementById("theme-toggle");

    function aplicarTema(claro) {
        document.body.classList.toggle("light-mode", claro);
        if (boton) {
            boton.textContent = claro ? "🌙" : "☀️";
        }
    }

    // Al cargar: usar el tema guardado
    let temaGuardado = null;
    try {
        temaGuardado = localStorage.getItem("theme");
    } catch (e) {}
    aplicarTema(temaGuardado === "light");

    // Al hacer click: cambiar y guardar
    if (boton) {
        boton.addEventListener("click", function () {
            const claro = !document.body.classList.contains("light-mode");
            try {
                localStorage.setItem("theme", claro ? "light" : "dark");
            } catch (e) {}
            aplicarTema(claro);
        });
    }
});