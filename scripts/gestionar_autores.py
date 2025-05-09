from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Autor

# Configuración de la base de datos
engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()

def listar_autores():
    autores = session.query(Autor).all()
    for autor in autores:
        print(f"ID: {autor.id}, Nombre: {autor.nombre}")

def agregar_autor(nombre):
    nuevo_autor = Autor(nombre=nombre)
    session.add(nuevo_autor)
    session.commit()
    print(f"Autor '{nombre}' agregado correctamente.")

def eliminar_autor(autor_id):
    autor = session.query(Autor).get(autor_id)
    if autor:
        session.delete(autor)
        session.commit()
        print(f"Autor con ID {autor_id} eliminado correctamente.")
    else:
        print(f"No se encontró un autor con ID {autor_id}.")

if __name__ == "__main__":
    listar_autores()
    # Ejemplo de uso:
    # agregar_autor("Nuevo Autor")
    # eliminar_autor(1)