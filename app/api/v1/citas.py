from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.cita import CitaCreate, CitaResponse
from app.crud.cita import (
    crear_cita,
    listar_citas,
    listar_citas_por_deportista,
    obtener_cita
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CitaResponse)
def crear(data: CitaCreate, db: Session = Depends(get_db)):
    return crear_cita(db, data)

@router.get("/", response_model=list[CitaResponse])
def listar(db: Session = Depends(get_db)):
    return listar_citas(db)

@router.get("/deportista/{deportista_id}", response_model=list[CitaResponse])
def listar_por_deportista(deportista_id: str, db: Session = Depends(get_db)):
    return listar_citas_por_deportista(db, deportista_id)

@router.get("/{cita_id}", response_model=CitaResponse)
def obtener(cita_id: str, db: Session = Depends(get_db)):
    cita = obtener_cita(db, cita_id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita
