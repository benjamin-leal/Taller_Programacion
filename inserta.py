from datetime import date, timedelta

from conexion import SessionLocal
from modelos import Reserva, Sala


def insertar():
    manana = date.today() + timedelta(days=1)  

    with SessionLocal() as session:
        sala = Sala(nombre="Sala A", capacidad=6, disponible=True)
        sala.reservas.append(Reserva(estudiante="Ana Pérez", fecha=manana))
        sala.reservas.append(Reserva(estudiante="Luis Soto", fecha=manana))

        session.add(sala)  
        session.commit()
        print("Datos insertados")


if __name__ == "__main__":
    insertar()