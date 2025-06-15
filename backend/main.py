from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from models import Cliente, Reserva, DatosCompletos
from datetime import date,time
from database import get_db
from database.get_db import Database
import psycopg2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/clientes/{id}")
def obtener_cliente(id: int, db: Database = Depends(get_db)):
    cliente = db.obtener_cliente(id)
    if cliente:
        return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.post("/reservas")
def crear_reserva(
    nombre: str = Form(...),
    apellido: str = Form(...),
    correo: str = Form(),
    empleado_id: str = Form(),
    servicio_id: int = Form(...),
    fecha_reserva: str = Form(...),
    hora_reserva: str = Form(...),
    db: Database = Depends(get_db)):
    
    if not db.comprobar_correo(correo):
        nuevoCliente = Cliente(nombre = nombre,
                        apellido = apellido,
                        correo = correo)
        
        cliente_id = db.crear_cliente(nuevoCliente)
    else:
          
        datos_cliente = db.comprobar_correo(correo)
        cliente_id = datos_cliente['id']
    
    try:

        if cliente_id:
            datosReserva = Reserva(
            cliente_id=cliente_id,
            empleado_id=empleado_id,
            servicio_id=servicio_id,
            fecha_reserva=fecha_reserva,
            hora_reserva=hora_reserva
            )
            reserva_id = db.crear_reserva(datosReserva)
            return {"mensaje": f"Le recordamos que su código de cliente es el {cliente_id}"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/reservas/{id}/cancelar")
def cancelar_reserva(id: int, db: Database = Depends(get_db)):
    try:
        db.cancelar_reserva(id)
        return {"mensaje": "Reserva cancelada exitosamente"}
    except psycopg2.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/reservas")
def listar_reservas(cliente_id: int, db: Database = Depends(get_db)):
    try:
        datos = db.obtener_reservas_cliente(cliente_id)
        reservas = [{'id_reserva' : row['id'],
                    'empleado' : row['empleado'],
                    'servicio' : row['servicio'],
                    'fecha' : row['fecha_reserva'],
                    'hora' : row['hora_reserva'],
                    'cliente' :row['nombre_cliente'],
                    'apellido_cliente' : row['apellido_cliente']}
                    for row in datos]
    
        return reservas
    except psycopg2.Error as e:
        raise HTTPException(status_code=400, detail=str(e))
        

@app.get("/servicios")
def listar_servicios(db: Database = Depends(get_db)):
    return db.listar_servicios()

@app.get("/empleados")
def listar_empleados(db: Database = Depends(get_db)):
    return db.listar_empleados()
