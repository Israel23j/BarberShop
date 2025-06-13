

document.addEventListener("DOMContentLoaded",function(){

    document.getElementById("boton-buscar").addEventListener("click", async ()=>{
        let codigo_reserva = document.getElementById("campo-busqueda").value
        codigo_reserva = parseInt(codigo_reserva)
        console.log(typeof codigo_reserva)
        try{
            response = await fetch("http://localhost:8000/reservas?cliente_id="+codigo_reserva)
            if (response.ok && response.length != 0){
                let reservas = await response.json()

                console.log(reservas)
                const lista_reservas = document.getElementById("lista_reservas");
                lista_reservas.innerHTML = ''; // Limpiar cualquier proyecto existente
                if (Array.isArray(reservas) && reservas.length > 0) {
                    reservas.forEach(reserva => {
                        const tarjeta_reserva = document.createElement("div");
                        tarjeta_reserva.id = "tarjeta_reserva" 
                        tarjeta_reserva.className = `tarjeta_reserva w-full 
                                                        sm:max-w-md lg:max-w-full 
                                                        mx-auto 
                                                        bg-white rounded-2xl shadow-lg 
                                                        p-4 sm:p-6 mb-6 
                                                        border border-gray-200 
                                                        flex flex-col justify-between`;

                        const info_reserva = document.createElement("div");
                        info_reserva.className = "info_reserva space-y-3 flex-grow";

                        // Asegurarse de que cada propiedad exista
                        const codigo_reserva = document.createElement("div");
                        codigo_reserva.className = "codigo_reserva text-xs sm:text-sm text-gray-500";
                        codigo_reserva.id = reserva.id_reserva
                        codigo_reserva.textContent = `Código de reserva: ${reserva.id_reserva}`; // Validar

                        const servicio = document.createElement("div");
                        servicio.className = "servicio text-sm sm:text-base text-gray-700";
                        servicio.textContent = `Tipo de servicio: ${reserva.servicio|| "Fecha No Disponible"}`; // Validar

                        const empleado = document.createElement("div");
                        empleado.className = "empleado text-base sm:text-lg font-semibold text-gray-800";
                        empleado.textContent = `Empleado: ${reserva.empleado}`; // Validar

                        const fecha_reserva = document.createElement("div");
                        fecha_reserva.className = "fecha text-sm sm:text-base text-gray-700";
                        fecha_reserva.textContent = `Fecha: ${reserva.fecha|| "Fecha No Disponible"}`; // Validar

                        const fila_hora_boton = document.createElement("div");
                        fila_hora_boton.className = "hora-boton flex justify-between items-center mt-4";

                        const hora_reserva = document.createElement("div");
                        hora_reserva.className = "hora text-sm sm:text-base text-gray-700";
                        hora_reserva.textContent = `Hora: ${reserva.hora}`; // Validar


                        // Botón Cancelar
                        const boton_cancelar = document.createElement("button");
                        boton_cancelar.className = `boton-cancelar px-3 sm:px-4 py-2 
                                                    bg-red-500 hover:bg-red-600 
                                                    text-white text-xs sm:text-sm 
                                                    font-medium rounded-md 
                                                    transition duration-300`;
                        boton_cancelar.textContent = "Cancelar";

                        info_reserva.appendChild(codigo_reserva);
                        info_reserva.appendChild(servicio);
                        info_reserva.appendChild(empleado);
                        info_reserva.appendChild(fecha_reserva);
                        info_reserva.appendChild(hora_reserva);
                        fila_hora_boton.appendChild(hora_reserva);
                        fila_hora_boton.appendChild(boton_cancelar);
                        info_reserva.appendChild(fila_hora_boton)
                        tarjeta_reserva.appendChild(info_reserva);
                        lista_reservas.appendChild(tarjeta_reserva)
                    })
                }



            }else{
                alert("no Hay reservas con asociadas a este código")
            }
        }catch(error){
            console.error("error: ", error)
        }


    })

    document.getElementById("lista_reservas").addEventListener("click", async (evento) => {
        if (evento.target.classList.contains("boton-cancelar")) {
            // Subimos desde el botón a la tarjeta
            const tarjeta = evento.target.closest("#tarjeta_reserva");
            
            // Obtenemos el div con clase 'codigo_reserva' dentro de esa tarjeta
            const codigoElemento = tarjeta.querySelector(".codigo_reserva");
            const id_reserva = codigoElemento.id;

            if (!confirm(`¿Estás seguro de cancelar la reserva ${id_reserva}?`)) return;

                try {
                    const respuesta = await fetch(`http://localhost:8000/reservas/${id_reserva}/cancelar`, {
                    method: "DELETE",
                    });

                    if (respuesta.ok) {
                        tarjeta.remove(); // Eliminar visualmente la tarjeta
                        console.log(`Reserva ${id_reserva} cancelada`);
                    } else {
                        console.error("Error al cancelar:", await respuesta.text());
                        alert("Error al cancelar la reserva");
                    }
                } catch (error) {
                    console.error("Error de red:", error);
                    alert("No se pudo conectar con el servidor");
                }
        }
    });

})