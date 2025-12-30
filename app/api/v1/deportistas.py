from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.deportista import DeportistaCreate, DeportistaResponse
from app.crud.deportista import crear_deportista, listar_deportistas, obtener_deportista

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=DeportistaResponse)
def crear(data: DeportistaCreate, db: Session = Depends(get_db)):
    try:
        return crear_deportista(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al crear deportista")

@router.get("", response_model=list[DeportistaResponse])
def listar(db: Session = Depends(get_db)):
    return listar_deportistas(db)

@router.get("/{deportista_id}", response_model=DeportistaResponse)
def obtener(deportista_id: str, db: Session = Depends(get_db)):
    deportista = obtener_deportista(db, deportista_id)
    if not deportista:
        raise HTTPException(status_code=404, detail="Deportista no encontrado")
    return deportista
