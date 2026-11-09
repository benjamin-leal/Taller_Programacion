from sqlalchemy import select

from conexion import SessionLocal
from modelos import Reserva, Sala


def consultar():
    with SessionLocal() as session:
        
        for sala in session.scalars(select(Sala)):
            print(sala.nombre, "->", [r.estudiante for r in sala.reservas])

        
        stmt = (
            select(Sala.nombre, Reserva.estudiante, Reserva.fecha)
            .join(Reserva)
            .where(Sala.disponible.is_(True))
        )
        for nombre, estudiante, fecha in session.execute(stmt):
            print(nombre, estudiante, fecha)


if __name__ == "__main__":
    consultar()