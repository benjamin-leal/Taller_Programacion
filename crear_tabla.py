from conexion import Base, engine
import modelos  


def crear_tablas():
    Base.metadata.create_all(engine)
    print("Tablas creadas")


if __name__ == "__main__":
    crear_tablas()