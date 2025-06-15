import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import date
from models import Cliente, Reserva

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="database",
            database="barbershop",
            user="postgres",
            password="Israel2025!"
        )
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def crear_cliente(self, cliente: Cliente)->int:
        self.cur.execute(
            """
            INSERT INTO clientes (nombre, apellido, correo)
            VALUES (%s, %s, %s) RETURNING id
            """,
            (cliente.nombre, cliente.apellido, cliente.correo)
        )
        cliente = self.cur.fetchone()
        cliente_id = cliente["id"]
        self.conn.commit()
        
        return cliente_id

    def crear_reserva(self, reserva: Reserva):
        self.cur.execute(
            """
            INSERT INTO reservas (cliente_id, empleado_id, servicio_id, fecha_reserva, hora_reserva)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
            """,
            (
                reserva.cliente_id,
                reserva.empleado_id,
                reserva.servicio_id,
                reserva.fecha_reserva,
                reserva.hora_reserva
            )
        )
        
        reserva = self.cur.fetchone()
        reserva_id = reserva['id']
        self.conn.commit()
        
        return reserva_id

    def listar_servicios(self):
        self.cur.execute("""SELECT * FROM servicios""")
        return self.cur.fetchall()

    def listar_empleados(self):
        self.cur.execute("""SELECT * FROM empleados""")
        return self.cur.fetchall()
    
    #def obtener_id(self, cliente: Cliente):
    #    self.cur.execute(f"""SELECT id FROM clientes WHERE correo '{cliente.correo}'""")

    def obtener_reservas_cliente(self, cliente_id: int):
        self.cur.execute(f"""SELECT reservas.id, empleados.nombre AS empleado, clientes.nombre AS nombre_cliente,clientes.apellido AS apellido_cliente,servicios.nombre AS servicio, reservas.fecha_reserva, reservas.hora_reserva
                            FROM reservas
                            JOIN empleados ON reservas.empleado_id = empleados.id
                            JOIN clientes ON reservas.cliente_id = clientes.id 
                            JOIN servicios ON reservas.servicio_id = servicios.id
                            WHERE reservas.cliente_id = {cliente_id}""")
        reservas = self.cur.fetchall()
        return reservas

    def cancelar_reserva(self, reserva_id: int):
        self.cur.execute(f"""DELETE FROM reservas WHERE id = {reserva_id}"""
        )
        self.conn.commit()

    def obtener_cliente(self, cliente_id: int):
        self.cur.execute("""SELECT * FROM clientes WHERE id = %s""", (cliente_id,))
        return self.cur.fetchone()
    
    def comprobar_correo(self,correo: str):
        self.cur.execute(f"""SELECT * FROM clientes WHERE correo = '{correo}'""")
        existe_cliente = self.cur.fetchone()
        
        return existe_cliente
