
/**Valida form */
$('#btnRegistro').on('click', function(e){

    e.preventDefault();

    nombreCliente = $('#nombreCliente');
    nombreUsuario = $('#nombreUsuario');
    emailUsuario = $('#emailUsuario');
    contrasena = $('#contrasena');

    if(validaFormulario()){
        alertify.alert('Usuario registrado exitosamente', `Bienvenido "${nombreUsuario.val()}"`);
        setTimeout(() => {
            window.location.href = '../login';
        }, 2000);
    }

});

function validaFormulario(){
    
    /**valida nombre */
    if(nombreCliente.val() == ''){
        
        nombreCliente.css('border-color', 'red');
        alertify.error('Debe ingresar su nombre')

        setTimeout(() => {
            nombreCliente.css('border-color', '');
        }, 2000);
        return false;
    }else{
        nombreCliente.css('border-color', 'green');
    }
    /**valida nombre usuario */
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

    /** valida email */
    if(emailUsuario.val() == ''){
        emailUsuario.css('border-color','red');
        alertify.error('Debe ingresar un email');
        setTimeout(() => {
            emailUsuario.css('border-color', '');
        }, 2000);
        return false;    
    }else{
        if(validarEmail(emailUsuario.val())){
            emailUsuario.css('border-color','green');
        }else{
            alertify.error('Email no valido, intente con otro');
            return false;
        }
        
    }

    /** valida contraseña */
    if(contrasena.val() == ''){
        contrasena.css('border-color','red');
        alertify.error('Debe ingresar su contraseña');
        setTimeout(() => {
            contrasena.css('border-color', '');
        }, 2000);
        return false;    
    }else if( contrasena.val().length <= 6){
        alertify.error('La contraseña debe tener mas de 6 caracteres')
        return false;
    }else{
        contrasena.css('border-color','green');
    }

    return true;
}

/**function valida email */
function validarEmail( email ) {
    expr = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    return expr.test(email)
        
}