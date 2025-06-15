
  document.addEventListener("DOMContentLoaded", ()=>{
    document.getElementById('formulario-reserva').addEventListener('submit', async function (e) {
        e.preventDefault(); // Evita que se recargue la página

        // Captura los datos del formulario
        const formData = new FormData(this);

        try {
            const response = await fetch('http://localhost:8000/reservas', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Error al enviar la reserva');
            }

            const resultado = await response.json();
            alert(resultado.mensaje || "Reserva enviada con éxito");
            
            //location.href = "./index.html"

        } catch (error) {
            
            console.error(error);
        }
    });
  })


