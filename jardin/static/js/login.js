



/**Valida form */
$('#btnIngreso').on('click', function(e){

    e.preventDefault();

    nombreUsuario = $('#nombreUsuario');
    contrasena = $('#contrasena');
    

    if(validaFormulario()){
        alertify.alert('Inicio de sesión exitoso', `Bienvenido "${nombreUsuario.val()}"`);
        setTimeout(() => {
            window.location.href = '../';
        }, 2000);
    }

});

function validaFormulario(){
    
    /**valida nombre */
    if(nombreUsuario.val() == ''){
        
        nombreUsuario.css('border-color', 'red');
        alertify.error('Debe ingresar un nombre de usuario')

        setTimeout(() => {
            nombreUsuario.css('border-color', '');
        }, 2000);
        return false;
    }else{
        nombreUsuario.css('border-color', 'green');
    }

    if(contrasena.val() == ''){
        contrasena.css('border-color','red');
        alertify.error('Debe ingresar su contraseña');
        setTimeout(() => {
            contrasena.css('border-color', '');
        }, 2000);
        return false;    
    }

    return true;
}