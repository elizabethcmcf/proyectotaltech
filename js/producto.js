document.addEventListener("DOMContentLoaded", function() {
    document.addEventListener("submit", function(event) {
        event.preventDefault();
        let caja = document.getElementById("ficha");
        let producto = document.querySelector("input[name='producto']:checked").value.toUpperCase();
        ficha.innerHTML="";

fetch ("productos.json")
        .then(respuesta => respuesta.json())
        .then(datos=>{
              for (let i in datos){
                if(datos[i].nombre.toUpperCase() == producto){
                    ficha.innerHTML=`<strong>El producto seleccionado es ${datos[i].nombre}.</strong><br><br>
                    <strong>FICHA TÉCNICA</strong><br><br>
                    <strong>Nuestra presentación:</strong> ${datos[i].presentacion}<br><br>
                    <strong>Almacenamiento recomendado:</strong> ${datos[i].almacenamiento_recomendado}<br><br>
                    <strong>Vida a temperatura ambiente:</strong> ${datos[i].vida_ambiente}<br><br>
                    <strong>Vida bajo refrigeración:</strong> ${datos[i].vida_refrigeracion}<br><br>
                    <strong>Impacto ambiental del cultivo:</strong> ${datos[i].impacto_ambiental}<br><br>
                    <strong>Descripción:</strong> ${datos[i].descripcion}<br><br>
                    <strong>Usos recomendados:</strong><br>
                    <ul>
                    ${datos[i].usos.map(uso => `<li>${uso}</li>`).join("")}
                    </ul>
                    `;
                }
            }
           
        });
});
});