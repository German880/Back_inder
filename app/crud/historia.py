from app.models.historia import HistoriaClinica, HistoriaClinicaJSON
from app.models.formulario import RespuestaGrupo, FormularioRespuesta
from app.models.deportista import Deportista
from app.models.archivo import ArchivoClinico
from datetime import date
from uuid import uuid4

def crear_historia(db, deportista_id):
    historia = HistoriaClinica(deportista_id=deportista_id)
    db.add(historia)
    db.commit()
    db.refresh(historia)
    return historia

def obtener_historias_por_deportista(db, deportista_id):
    return db.query(HistoriaClinica).filter(
        HistoriaClinica.deportista_id == deportista_id
    ).all()

def obtener_historia_completa(db, historia_id):
    historia = db.query(HistoriaClinica).filter(
        HistoriaClinica.id == historia_id
    ).first()

    if not historia:
        return None

    deportista = db.query(Deportista).filter(
        Deportista.id == historia.deportista_id
    ).first()

    grupos = db.query(RespuestaGrupo).filter(
        RespuestaGrupo.historia_clinica_id == historia_id
    ).all()

    formularios = []
    for grupo in grupos:
        respuestas = db.query(FormularioRespuesta).filter(
            FormularioRespuesta.grupo_id == grupo.id
        ).all()

        formularios.append({
            "formulario_id": grupo.formulario_id,
            "respuestas": [
                {"campo": r.campo, "valor": r.valor}
                for r in respuestas
            ]
        })

    archivos = db.query(ArchivoClinico).filter(
        ArchivoClinico.historia_id == historia_id
    ).all()

    return {
        "historia": {
            "id": historia.id,
            "fecha_apertura": historia.fecha_apertura
        },
        "deportista": {
            "id": deportista.id,
            "documento": deportista.documento,
            "nombres": deportista.nombres,
            "apellidos": deportista.apellidos
        },
        "formularios": formularios,
        "archivos": [
            {
                "id": a.id,
                "nombre_original": a.nombre_original,
                "categoria": a.categoria,
                "tipo_archivo": a.tipo_archivo,
                "ruta": a.ruta,
                "fecha_subida": a.fecha_subida
            }
            for a in archivos
        ]
    }

def crear_historia_completa(db, data):
    """
    Crear una historia clínica completa con todos los 7 pasos
    
    Args:
        db: Sesión de base de datos
        data: HistoriaClinicaCompleteCreate con todos los datos
    
    Returns:
        Diccionario con el ID de la historia creada
    """
    try:
        # 1. Crear historia clínica básica
        historia = HistoriaClinica(
            deportista_id=data.deportista_id,
            fecha_apertura=date.today(),
            estado_id="01b6e2e1-2c3d-4a5b-9c8d-1e2f3g4h5i6j"  # "Abierta"
        )
        db.add(historia)
        db.flush()  # Obtener el ID generado
        
        # 2. Guardar datos completos como JSON
        datos_json = HistoriaClinicaJSON(
            historia_clinica_id=str(historia.id),
            deportista_id=str(data.deportista_id),
            datos_completos=data.model_dump()
        )
        db.add(datos_json)
        
        # 3. Commit
        db.commit()
        db.refresh(historia)
        
        return {
            "id": str(historia.id),
            "deportista_id": str(data.deportista_id),
            "fecha_apertura": historia.fecha_apertura.isoformat(),
            "message": "Historia clínica creada exitosamente"
        }
        
    except Exception as e:
        db.rollback()
        raise ValueError(f"Error al crear historia clínica: {str(e)}")

def obtener_historia_datos_completos(db, historia_id: str) -> dict:
    """
    Obtener historia clínica completa con todos los datos
    
    Args:
        db: Sesión de base de datos
        historia_id: ID de la historia clínica
    
    Returns:
        Datos completos de la historia clínica
    """
    historia_json = db.query(HistoriaClinicaJSON).filter(
        HistoriaClinicaJSON.historia_clinica_id == historia_id
    ).first()
    
    if not historia_json:
        raise ValueError(f"Historia clínica con ID {historia_id} no encontrada")
    
    return historia_json.datos_completos
