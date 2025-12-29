from app.models.deportista import Deportista

def crear_deportista(db, data):
    deportista = Deportista(**data.dict())
    db.add(deportista)
    db.commit()
    db.refresh(deportista)
    return deportista

def listar_deportistas(db):
    return db.query(Deportista).all()

def obtener_deportista(db, deportista_id):
    return db.query(Deportista).filter(Deportista.id == deportista_id).first()
