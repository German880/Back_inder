from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.core.dependencies import get_db
from app.schemas.deportista import DeportistaCreate, DeportistaUpdate, DeportistaResponse
from app.crud.deportista import crear_deportista, listar_deportistas, obtener_deportista, eliminar_deportista, actualizar_deportista
from app.models.deportista import Deportista

router = APIRouter()

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

@router.get("/search", response_model=list[DeportistaResponse])
def buscar(q: str = Query(...), db: Session = Depends(get_db)):
    """Buscar deportistas por nombre, apellido o documento"""
    q = q.strip()
    if not q or len(q) < 2:
        raise HTTPException(status_code=400, detail="El término de búsqueda debe tener al menos 2 caracteres")
    
    resultados = db.query(Deportista).filter(
        or_(
            Deportista.nombres.ilike(f"%{q}%"),
            Deportista.apellidos.ilike(f"%{q}%"),
            Deportista.numero_documento.ilike(f"%{q}%")
        )
    ).limit(10).all()
    
    return resultados

@router.get("/{deportista_id}", response_model=DeportistaResponse)
def obtener(deportista_id: str, db: Session = Depends(get_db)):
    deportista = obtener_deportista(db, deportista_id)
    if not deportista:
        raise HTTPException(status_code=404, detail="Deportista no encontrado")
    return deportista

@router.put("/{deportista_id}", response_model=DeportistaResponse)
def actualizar(deportista_id: str, data: DeportistaUpdate, db: Session = Depends(get_db)):
    """Actualizar un deportista existente"""
    try:
        deportista = actualizar_deportista(db, deportista_id, data)
        if not deportista:
            raise HTTPException(status_code=404, detail="Deportista no encontrado")
        return deportista
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al actualizar deportista")

@router.delete("/{deportista_id}", status_code=204)
def eliminar(deportista_id: str, db: Session = Depends(get_db)):
    """Eliminar un deportista por ID"""
    success = eliminar_deportista(db, deportista_id)
    if not success:
        raise HTTPException(status_code=404, detail="Deportista no encontrado")
