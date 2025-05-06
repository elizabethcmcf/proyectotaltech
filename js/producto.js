document.addEventListener("DOMContentLoaded",function(){
    document.addEventListener("submit",function(event){
        event.preventDefault()
        let caja=document.getElementById("ficha")
        let producto=document.getElementById("producto").value
        caja.innerHTML="El producto seleccionado es "+producto+"."
        })
    })