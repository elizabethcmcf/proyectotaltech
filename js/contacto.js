document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("validar").addEventListener("click",function(event){
        let nombre=document.getElementById("nombre").value
        let email=document.getElementById("email").value
        let tel=document.getElementById("tel").value
        let asunto=document.getElementById("asunto").value
        let msg=document.getElementById("msg").value
        let mensaje=`Nombre: ${nombre}\nEmail: ${email}\nTeléfono: ${tel}\nAsunto: ${asunto}\nMensaje: ${msg}`;  
        alert("Se enviará esta información a ALCAM:\n"+mensaje+".\n Si el mensaje se encuentra correcto haga clic en Aceptar y luego en gitel botón Enviar.")
        })
    })