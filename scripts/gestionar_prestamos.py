from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Prestamo, Libro, Usuario
from datetime import date

# Configuración de la base de datos
engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()

def listar_prestamos():
    prestamos = session.query(Prestamo).all()
    for prestamo in prestamos:
        print(f"ID: {prestamo.id}, Libro: {prestamo.libro.titulo}, Usuario: {prestamo.usuario.nombre}, Fecha Préstamo: {prestamo.fecha_prestamo}, Fecha Devolución: {prestamo.fecha_devolucion}")

def registrar_prestamo(libro_id, usuario_id):
    libro = session.query(Libro).get(libro_id)
    usuario = session.query(Usuario).get(usuario_id)
    if libro and usuario and libro.disponible:
        nuevo_prestamo = Prestamo(libro_id=libro_id, usuario_id=usuario_id, fecha_prestamo=date.today())
        libro.disponible = False
        session.add(nuevo_prestamo)
        session.commit()
        print(f"Préstamo registrado correctamente para el libro '{libro.titulo}'.")
    else:
        print("El libro no está disponible o el usuario no existe.")

def devolver_prestamo(prestamo_id):
    prestamo = session.query(Prestamo).get(prestamo_id)
    if prestamo and not prestamo.fecha_devolucion:
        prestamo.fecha_devolucion = date.today()
        prestamo.libro.disponible = True
        session.commit()
        print(f"Préstamo con ID {prestamo_id} devuelto correctamente.")
    else:
        print("El préstamo no existe o ya fue devuelto.")

if __name__ == "__main__":
    listar_prestamos()
    # Ejemplo de uso:
    # registrar_prestamo(1, 1)
    # devolver_prestamo(1)