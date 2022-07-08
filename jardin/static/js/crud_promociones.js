

formato = new Intl.NumberFormat('es-CL', { 
    style: 'currency', 
    currency: 'CLP' 
})

precioNuevo = $('#precioNuevo')

$('#precioNuevo').on('focusout', function(){
    precioFormato = formato.format(precioNuevo.val())
    precioNuevo.val(precioFormato)
})




/**Valida form */
$('#btnGuardar').on('click', function(e){

    e.preventDefault();

    eligeProducto = $('#eligeProducto').find(":selected")
    porcentajeDesc = $('#porcentajeDesc')
    // precioNuevo = $('#precioNuevo')
    fechaCaduce = $('#fechaCaduce')

    


    mensajeError = $('#mensajeError');
    // mensajeError.hide();


    if(validaFormulario()){
        alertify.alert('Promoción agregada exitosamente', `Producto ${eligeProducto.text()}. Descuento: %${porcentajeDesc.val()}.`);
        setTimeout(() => {
            window.location.href = '../index';
        }, 3000);
    }

});

function validaFormulario(){
    
    /**valida producto */
    if(eligeProducto.val() == 0){
        
        eligeProducto.css('border-color', 'red');
        alertify.error('Debe elegir un producto para agregar promocion')

        setTimeout(() => {
            eligeProducto.css('border-color', '');
        }, 2000);
        return false;
    }else{
        eligeProducto.css('border-color', 'green');
    }

    /**valida procentaje */
    if(porcentajeDesc.val() == ''){
        porcentajeDesc.css('border-color', 'red');
        alertify.error('Debe agregar un porcentaje de descuento')

        setTimeout(() => {
            porcentajeDesc.css('border-color', '');
        }, 2000);
        return false;
    }else{
        porcentajeDesc.css('border-color', 'green');
    }

    /**valida precio nuevo */
    // if(precioNuevo.val() == ''){
    //     precioNuevo.css('border-color', 'red');
    //     alertify.error('Debe agregar el nuevo precio del producto')

    //     setTimeout(() => {
    //         precioNuevo.css('border-color', '');
    //     }, 2000);
    //     return false;
    // }else{
    //     precioNuevo.css('border-color', 'green');
    // }

    //valida fecha
    if(fechaCaduce.val() == ''){
    fechaCaduce.css('border-color', 'red');
    alertify.error('Debe introducir la fecha de caducidad de la promoción');

    setTimeout(() => {
        fechaCaduce.css('border-color', '');
    }, 2000);
        return false
    }else{
        fechaCaduce.css('border-color', 'green');
    }

    return true;
}