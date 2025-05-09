from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Libro, Autor

# Configuración de la base de datos
engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()

def listar_libros():
    libros = session.query(Libro).all()
    for libro in libros:
        print(f"ID: {libro.id}, Título: {libro.titulo}, Autor: {libro.autor.nombre}, Disponible: {'Sí' if libro.disponible else 'No'}")

def agregar_libro(titulo, autor_nombre):
    autor = session.query(Autor).filter_by(nombre=autor_nombre).first()
    if not autor:
        autor = Autor(nombre=autor_nombre)
        session.add(autor)
        session.commit()
    nuevo_libro = Libro(titulo=titulo, autor_id=autor.id)
    session.add(nuevo_libro)
    session.commit()
    print(f"Libro '{titulo}' agregado correctamente.")

def eliminar_libro(libro_id):
    libro = session.query(Libro).get(libro_id)
    if libro:
        session.delete(libro)
        session.commit()
        print(f"Libro con ID {libro_id} eliminado correctamente.")
    else:
        print(f"No se encontró un libro con ID {libro_id}.")

if __name__ == "__main__":
    listar_libros()
    # Ejemplo de uso:
    # agregar_libro("Nuevo Libro", "Autor Ejemplo")
    # eliminar_libro(1)