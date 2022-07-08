

formato = new Intl.NumberFormat('es-CL', { 
    style: 'currency', 
    currency: 'CLP' 
})

precioProducto = $('#precioProducto')

$('#precioProducto').on('focusout', function(){
    precioFormato = formato.format(precioProducto.val())
    precioProducto.val(precioFormato)
})

/**Valida form */
$('#btnAgregarProducto').on('click', function(e){

    e.preventDefault();

    nombreProducto = $('#nombreProducto')
    precioProducto = $('#precioProducto')
    stockProducto = $('#stockProducto')
    imagenProducto = $('#imagenProducto')


    mensajeError = $('#mensajeError');
    // mensajeError.hide();


    if(validaFormulario()){
        alertify.alert('Producto Guardado con éxito ', `Producto ${nombreProducto.val()}, guardado exitosamente. Stock: ${stockProducto.val()}. Precio: $${precioProducto.val()} `);
        setTimeout(() => {
            window.location.href = '../index';
        }, 3000);
    }

});

function validaFormulario(){
    
    /**valida nombre */
    if(nombreProducto.val() == ''){
        
        nombreProducto.css('border-color', 'red');
        alertify.error('El nombre no puede estar vacio')

        setTimeout(() => {
            nombreProducto.css('border-color', '');
        }, 2000);
        return false;
    }else{
        nombreProducto.css('border-color', 'green');
    }

    /**valida stock */
    if(precioProducto.val() == ''){
        precioProducto.css('border-color', 'red');
        alertify.error('El valor del producto no puede estar vacio')

        setTimeout(() => {
            precioProducto.css('border-color', '');
        }, 2000);
        return false;
    }else{
        precioProducto.css('border-color', 'green');
    }

    /**valida stock */
    if(stockProducto.val() == ''){
        stockProducto.css('border-color', 'red');
        alertify.error('El stock del producto no puede estar vacio')

        setTimeout(() => {
            stockProducto.css('border-color', '');
        }, 2000);
        return false;
    }else{
        stockProducto.css('border-color', 'green');
    }

    //valida imagen
    if(imagenProducto.val() == ''){
    imagenProducto.css('border-color', 'red');
    alertify.error('No ha seleccionado una imagen');

    setTimeout(() => {
        imagenProducto.css('border-color', '');
    }, 2000);
        return false;

    }else{
        imagenProducto.css('border-color', 'green');
    }

    return true;
}