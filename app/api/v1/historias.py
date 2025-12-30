from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.schemas.formulario_respuesta import FormularioRespuestaCreate
from app.crud.formulario import crear_grupo, guardar_respuesta
from app.schemas.historia import (
    HistoriaCreate, 
    HistoriaResponse,
    HistoriaClinicaCompleteCreate
)
from app.crud.historia import (
    crear_historia, 
    obtener_historias_por_deportista, 
    obtener_historia_completa,
    crear_historia_completa,
    obtener_historia_datos_completos
)

router = APIRouter()

@router.post("/completa")
def guardar_historia_completa(data: HistoriaClinicaCompleteCreate, db: Session = Depends(get_db)):
    """
    Guardar una historia clínica completa con todos los 7 pasos
    
    POST /api/v1/historias_clinicas/completa
    """
    try:
        resultado = crear_historia_completa(db, data)
        return resultado
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        import traceback
        print(f"Error en crear_historia_completa: {str(e)}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

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

@router.get("/{historia_id}/datos-completos")
def obtener_datos_historia(historia_id: str, db: Session = Depends(get_db)):
    """
    Obtener todos los datos de una historia clínica completa
    
    GET /api/v1/historias_clinicas/{historia_id}/datos-completos
    """
    try:
        datos = obtener_historia_datos_completos(db, historia_id)
        return {"success": True, "data": datos}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
