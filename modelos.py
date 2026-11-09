from datetime import date

from sqlalchemy import BOOLEAN, DATE, CheckConstraint, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from conexion import Base


class Sala(Base):
    __tablename__ = "sala"
    __table_args__ = (
        CheckConstraint("capacidad >= 0", name="ck_capacidad"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    disponible: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=True)

    reservas: Mapped[list["Reserva"]] = relationship(back_populates="sala")


class Reserva(Base):
    __tablename__ = "reserva"
    __table_args__ = (
        CheckConstraint("fecha >= CURRENT_DATE", name="ck_fecha"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    sala_id: Mapped[int] = mapped_column(ForeignKey("sala.id"), nullable=False)
    fecha: Mapped[date] = mapped_column(DATE, nullable=False)

    sala: Mapped["Sala"] = relationship(back_populates="reservas")