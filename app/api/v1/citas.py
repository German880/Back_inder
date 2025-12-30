from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.cita import CitaCreate, CitaUpdate, CitaResponse
from app.crud.cita import (
    crear_cita,
    listar_citas,
    listar_citas_por_deportista,
    obtener_cita,
    actualizar_cita,
    eliminar_cita,
)

router = APIRouter(prefix="/citas", tags=["citas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CitaResponse, status_code=201)
def crear(data: CitaCreate, db: Session = Depends(get_db)):
    """Crear una nueva cita"""
    try:
        return crear_cita(db, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear cita: {str(e)}")

@router.get("/", response_model=list[CitaResponse])
def listar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Listar todas las citas"""
    return listar_citas(db, skip, limit)

@router.get("/{cita_id}", response_model=CitaResponse)
def obtener(cita_id: str, db: Session = Depends(get_db)):
    """Obtener una cita por su ID"""
    cita = obtener_cita(db, cita_id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@router.put("/{cita_id}", response_model=CitaResponse)
def actualizar(cita_id: str, data: CitaUpdate, db: Session = Depends(get_db)):
    """Actualizar una cita"""
    cita = actualizar_cita(db, cita_id, data)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@router.delete("/{cita_id}", status_code=204)
def eliminar(cita_id: str, db: Session = Depends(get_db)):
    """Eliminar una cita"""
    success = eliminar_cita(db, cita_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cita no encontrada")

@router.get("/deportista/{deportista_id}", response_model=list[CitaResponse])
def listar_por_deportista(deportista_id: str, db: Session = Depends(get_db)):
    """Obtener citas de un deportista específico"""
    return listar_citas_por_deportista(db, deportista_id)
