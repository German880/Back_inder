from app.models.historia import HistoriaClinica
from app.models.formulario import RespuestaGrupo, RespuestaFormulario
from app.models.deportista import Deportista
from app.models.archivo import ArchivoClinico

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
        respuestas = db.query(RespuestaFormulario).filter(
            RespuestaFormulario.grupo_id == grupo.id
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
