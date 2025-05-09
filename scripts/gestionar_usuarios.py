from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Usuario

# Configuración de la base de datos
engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()

def listar_usuarios():
    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Documento: {usuario.documento_identidad}, Correo: {usuario.correo}")

def agregar_usuario(nombre, documento_identidad, correo):
    nuevo_usuario = Usuario(nombre=nombre, documento_identidad=documento_identidad, correo=correo)
    session.add(nuevo_usuario)
    session.commit()
    print(f"Usuario '{nombre}' agregado correctamente.")

def eliminar_usuario(usuario_id):
    usuario = session.query(Usuario).get(usuario_id)
    if usuario:
        session.delete(usuario)
        session.commit()
        print(f"Usuario con ID {usuario_id} eliminado correctamente.")
    else:
        print(f"No se encontró un usuario con ID {usuario_id}.")

if __name__ == "__main__":
    listar_usuarios()
    # Ejemplo de uso:
    # agregar_usuario("Juan Pérez", "12345678", "juan@example.com")
    # eliminar_usuario(1)