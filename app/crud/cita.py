from app.models.cita import Cita
from sqlalchemy import desc

def crear_cita(db, data):
    """Crear una nueva cita"""
    cita = Cita(
        deportista_id=data.deportista_id,
        fecha=data.fecha,
        hora=data.hora,
        tipo_cita_id=data.tipo_cita_id,
        estado_cita_id=data.estado_cita_id,
        observaciones=data.observaciones
    )
    db.add(cita)
    db.commit()
    db.refresh(cita)
    return cita

def listar_citas(db, skip: int = 0, limit: int = 100):
    """Listar todas las citas ordenadas por fecha"""
    return db.query(Cita).order_by(Cita.fecha, Cita.hora).offset(skip).limit(limit).all()

def listar_citas_por_deportista(db, deportista_id):
    """Listar citas de un deportista específico"""
    return db.query(Cita).filter(
        Cita.deportista_id == deportista_id
    ).order_by(Cita.fecha, Cita.hora).all()

def obtener_cita(db, cita_id):
    """Obtener una cita por su ID"""
    return db.query(Cita).filter(Cita.id == cita_id).first()

def actualizar_cita(db, cita_id, data):
    """Actualizar una cita"""
    cita = obtener_cita(db, cita_id)
    if not cita:
        return None
    
    # Actualizar solo los campos proporcionados
    update_data = data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(cita, field, value)
    
    db.commit()
    db.refresh(cita)
    return cita

def eliminar_cita(db, cita_id):
    """Eliminar una cita"""
    cita = obtener_cita(db, cita_id)
    if not cita:
        return False
    
    db.delete(cita)
    db.commit()
    return True
