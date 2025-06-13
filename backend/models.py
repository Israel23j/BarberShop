from pydantic import BaseModel
from datetime import date,time

class Cliente(BaseModel):
    nombre: str
    apellido: str
    correo: str

class Reserva(BaseModel):
    cliente_id: int
    empleado_id: int
    servicio_id: int
    fecha_reserva: str  # formato 'YYYY-MM-DD'
    hora_reserva: str   # formato 'HH:MM:SS'

class DatosCompletos(BaseModel):
    nombre: str 
    apellido: str
    correo: str
    empleado_id: int
    servicio_id: int
    fecha_reserva: date  # formato 'YYYY-MM-DD'
    hora_reserva: time   # formato 'HH:MM:SS'
