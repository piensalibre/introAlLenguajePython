function mueveReloj(){
    momentoActual = new Date()
    hora = momentoActual.getHours()
    minuto = momentoActual.getMinutes()
    segundo = momentoActual.getSeconds()

    horaImprimible = hora + " : " + minuto + " : " + segundo
    return horaImprimible
    
}
alert(mueveReloj());

$(document).ready(function(){
    function ajaxLogin(){
        $.ajax({
                url:'/ajaxLogin',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response){
                    console.log(response);
                    alert(response);
                },
                error: function(){
                    console.log("error");
                }
            });
    }
    $("#loginForm").submit(function(event){
        event.preventDefault();
        ajaxLogin();
    });
});