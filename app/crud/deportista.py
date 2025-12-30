from app.models.deportista import Deportista
from sqlalchemy.exc import IntegrityError

def crear_deportista(db, data):
    try:
        # Crear el objeto deportista
        deportista = Deportista(**data.dict())
        
        # Agregar a la sesión
        db.add(deportista)
        
        # Hacer commit de la transacción
        db.commit()
        
        return deportista
    except IntegrityError as e:
        db.rollback()
        # Detectar si es un error de documento duplicado
        if "numero_documento" in str(e):
            raise ValueError("El número de documento ya existe en el sistema")
        raise ValueError(f"Error de integridad en la base de datos: {str(e)}")
    except Exception as e:
        db.rollback()
        raise

def listar_deportistas(db):
    return db.query(Deportista).all()

def obtener_deportista(db, deportista_id):
    return db.query(Deportista).filter(Deportista.id == deportista_id).first()
