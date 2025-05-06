document.addEventListener("DOMContentLoaded",function(){
    document.addEventListener("submit",function(event){
        event.preventDefault()
        let nombre=document.getElementById("nombre").value
        let email=document.getElementById("email").value
        let tel=document.getElementById("tel").value
        let asunto=document.getElementById("asunto").value
        let msg=document.getElementById("msg").value
        let mensaje=`Nombre: ${nombre}\nEmail: ${email}\nTeléfono: ${tel}\nAsunto: ${asunto}\nMensaje: ${msg}`  
        let url=`https://api.whatsapp.com/send?phone=5491155555555&text=${encodeURIComponent(mensaje)}`
        window.open(url,"_blank")

        })
    })