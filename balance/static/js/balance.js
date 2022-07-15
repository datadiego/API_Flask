function cargarMovimientos() {
console.log("HAS LLAMADO A CARGAR A TU PUTA MADRE");
const tabla = document.querySelector("#cuerpo-tabla");
const html = "<tr><td>05/01/2022</td></tr>";
  tabla.addEventListener("click", cargarMovimientos);
  tabla.innerHTML = html; 
}

window.onload = function(){
  const boton = document.querySelector("#boton-recarga")
  boton.addEventListener("click", cargarMovimientos)
}


