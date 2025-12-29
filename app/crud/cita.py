from app.models.cita import Cita

def crear_cita(db, data):
    cita = Cita(**data.dict())
    db.add(cita)
    db.commit()
    db.refresh(cita)
    return cita

def listar_citas(db):
    return db.query(Cita).order_by(Cita.fecha_inicio).all()

def listar_citas_por_deportista(db, deportista_id):
    return db.query(Cita).filter(
        Cita.deportista_id == deportista_id
    ).order_by(Cita.fecha_inicio).all()

def obtener_cita(db, cita_id):
    return db.query(Cita).filter(Cita.id == cita_id).first()
