from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.formulario_respuesta import FormularioRespuestaCreate
from app.crud.formulario import crear_grupo, guardar_respuesta
from app.schemas.historia import HistoriaCreate, HistoriaResponse
from app.crud.historia import crear_historia, obtener_historias_por_deportista, obtener_historia_completa

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=HistoriaResponse)
def crear(data: HistoriaCreate, db: Session = Depends(get_db)):
    return crear_historia(db, data.deportista_id)

@router.get("/deportista/{deportista_id}", response_model=list[HistoriaResponse])
def listar_por_deportista(deportista_id: str, db: Session = Depends(get_db)):
    return obtener_historias_por_deportista(db, deportista_id)

@router.post("/{historia_id}/formularios")
def guardar_formulario(historia_id: str, data: FormularioRespuestaCreate, db: Session = Depends(get_db)):
    grupo = crear_grupo(db, historia_id, data.formulario_id)
    for r in data.respuestas:
        guardar_respuesta(db, grupo.id, r.campo, r.valor)
    db.commit()
    return {"status": "ok"}

@router.get("/{historia_id}/completa")
def historia_completa(historia_id: str, db: Session = Depends(get_db)):
    data = obtener_historia_completa(db, historia_id)
    if not data:
        raise HTTPException(status_code=404, detail="Historia clínica no encontrada")
    return data
