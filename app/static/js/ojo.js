document.querySelectorAll('.eye-icon').forEach(function(eyeIcon) {
    eyeIcon.addEventListener('click', function () {
        const passwordField = this.previousElementSibling;  // Encuentra el campo de contraseña
        if (passwordField.type === 'password') {
            passwordField.type = 'text'; // Muestra la contraseña
        } else {
            passwordField.type = 'password'; // Oculta la contraseña
        }
    });
});
