"""
CRUD operations para Historia Clínica - Datos normalizados
"""
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.antecedentes import (
    AntecedentesPersonales, AntecedentesFamiliares, LesioneDeportivas,
    CirugiasPrivas, Alergias, Medicaciones, VacunasAdministradas,
    RevisionSistemas, SignosVitales, PruebasComplementarias,
    Diagnosticos, PlanTratamiento, RemisionesEspecialistas
)
from app.schemas.antecedentes import (
    AntecedentesPersonalesCreate, AntecedentesFamiliaresCreate,
    LesioneDeportavasCreate, CirugiasPrivasCreate, AlergiasCreate,
    MedicacionesCreate, VacunasAdministradasCreate, RevisionSistemasCreate,
    SignosVitalesCreate, PruebasComplementariasCreate, DiagnosticosCreate,
    PlanTratamientoCreate, RemisionesEspecialistasCreate
)


# ============================================================================
# ANTECEDENTES PERSONALES
# ============================================================================

def crear_antecedente_personal(db: Session, data: AntecedentesPersonalesCreate):
    db_obj = AntecedentesPersonales(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_antecedentes_personales(db: Session, historia_clinica_id: UUID):
    return db.query(AntecedentesPersonales).filter(
        AntecedentesPersonales.historia_clinica_id == historia_clinica_id
    ).all()


def eliminar_antecedente_personal(db: Session, antecedente_id: UUID):
    db.query(AntecedentesPersonales).filter(AntecedentesPersonales.id == antecedente_id).delete()
    db.commit()


# ============================================================================
# ANTECEDENTES FAMILIARES
# ============================================================================

def crear_antecedente_familiar(db: Session, data: AntecedentesFamiliaresCreate):
    db_obj = AntecedentesFamiliares(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_antecedentes_familiares(db: Session, historia_clinica_id: UUID):
    return db.query(AntecedentesFamiliares).filter(
        AntecedentesFamiliares.historia_clinica_id == historia_clinica_id
    ).all()


def eliminar_antecedente_familiar(db: Session, antecedente_id: UUID):
    db.query(AntecedentesFamiliares).filter(AntecedentesFamiliares.id == antecedente_id).delete()
    db.commit()


# ============================================================================
# LESIONES DEPORTIVAS
# ============================================================================

def crear_lesion_deportiva(db: Session, data: LesioneDeportavasCreate):
    db_obj = LesioneDeportivas(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_lesiones_deportivas(db: Session, historia_clinica_id: UUID):
    return db.query(LesioneDeportivas).filter(
        LesioneDeportivas.historia_clinica_id == historia_clinica_id
    ).all()


def eliminar_lesion_deportiva(db: Session, lesion_id: UUID):
    db.query(LesioneDeportivas).filter(LesioneDeportivas.id == lesion_id).delete()
    db.commit()


# ============================================================================
# CIRUGÍAS PREVIAS
# ============================================================================

def crear_cirugia(db: Session, data: CirugiasPrivasCreate):
    db_obj = CirugiasPrivas(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_cirugias(db: Session, historia_clinica_id: UUID):
    return db.query(CirugiasPrivas).filter(
        CirugiasPrivas.historia_clinica_id == historia_clinica_id
    ).all()


def eliminar_cirugia(db: Session, cirugia_id: UUID):
    db.query(CirugiasPrivas).filter(CirugiasPrivas.id == cirugia_id).delete()
    db.commit()


# ============================================================================
# ALERGIAS
# ============================================================================

def crear_alergia(db: Session, data: AlergiasCreate):
    db_obj = Alergias(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_alergias(db: Session, historia_clinica_id: UUID):
    return db.query(Alergias).filter(
        Alergias.historia_clinica_id == historia_clinica_id
    ).all()


def eliminar_alergia(db: Session, alergia_id: UUID):
    db.query(Alergias).filter(Alergias.id == alergia_id).delete()
    db.commit()


# ============================================================================
# MEDICACIONES
# ============================================================================

def crear_medicacion(db: Session, data: MedicacionesCreate):
    db_obj = Medicaciones(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_medicaciones(db: Session, historia_clinica_id: UUID):
    return db.query(Medicaciones).filter(
        Medicaciones.historia_clinica_id == historia_clinica_id
    ).all()


def eliminar_medicacion(db: Session, medicacion_id: UUID):
    db.query(Medicaciones).filter(Medicaciones.id == medicacion_id).delete()
    db.commit()


# ============================================================================
# VACUNAS ADMINISTRADAS
# ============================================================================

def crear_vacuna(db: Session, data: VacunasAdministradasCreate):
    db_obj = VacunasAdministradas(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_vacunas(db: Session, historia_clinica_id: UUID):
    return db.query(VacunasAdministradas).filter(
        VacunasAdministradas.historia_clinica_id == historia_clinica_id
    ).all()


def eliminar_vacuna(db: Session, vacuna_id: UUID):
    db.query(VacunasAdministradas).filter(VacunasAdministradas.id == vacuna_id).delete()
    db.commit()


# ============================================================================
# REVISIÓN POR SISTEMAS
# ============================================================================

def crear_revision_sistema(db: Session, data: RevisionSistemasCreate):
    db_obj = RevisionSistemas(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_revision_sistemas(db: Session, historia_clinica_id: UUID):
    return db.query(RevisionSistemas).filter(
        RevisionSistemas.historia_clinica_id == historia_clinica_id
    ).all()


def eliminar_revision_sistema(db: Session, revision_id: UUID):
    db.query(RevisionSistemas).filter(RevisionSistemas.id == revision_id).delete()
    db.commit()


# ============================================================================
# SIGNOS VITALES
# ============================================================================

def crear_signos_vitales(db: Session, data: SignosVitalesCreate):
    db_obj = SignosVitales(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_signos_vitales(db: Session, historia_clinica_id: UUID):
    return db.query(SignosVitales).filter(
        SignosVitales.historia_clinica_id == historia_clinica_id
    ).first()


def actualizar_signos_vitales(db: Session, historia_clinica_id: UUID, data: SignosVitalesCreate):
    sv = obtener_signos_vitales(db, historia_clinica_id)
    if sv:
        for key, value in data.dict().items():
            setattr(sv, key, value)
        db.commit()
        db.refresh(sv)
        return sv
    else:
        return crear_signos_vitales(db, data)


# ============================================================================
# PRUEBAS COMPLEMENTARIAS
# ============================================================================

def crear_prueba_complementaria(db: Session, data: PruebasComplementariasCreate):
    db_obj = PruebasComplementarias(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_pruebas_complementarias(db: Session, historia_clinica_id: UUID):
    return db.query(PruebasComplementarias).filter(
        PruebasComplementarias.historia_clinica_id == historia_clinica_id
    ).all()


def obtener_prueba_por_id(db: Session, prueba_id: UUID):
    return db.query(PruebasComplementarias).filter(
        PruebasComplementarias.id == prueba_id
    ).first()


def actualizar_prueba_complementaria(db: Session, prueba_id: UUID, data: PruebasComplementariasCreate):
    prueba = obtener_prueba_por_id(db, prueba_id)
    if prueba:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(prueba, key, value)
        db.commit()
        db.refresh(prueba)
    return prueba


def eliminar_prueba_complementaria(db: Session, prueba_id: UUID):
    db.query(PruebasComplementarias).filter(PruebasComplementarias.id == prueba_id).delete()
    db.commit()


# ============================================================================
# DIAGNÓSTICOS
# ============================================================================

def crear_diagnostico(db: Session, data: DiagnosticosCreate):
    db_obj = Diagnosticos(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_diagnosticos(db: Session, historia_clinica_id: UUID):
    return db.query(Diagnosticos).filter(
        Diagnosticos.historia_clinica_id == historia_clinica_id
    ).all()


def eliminar_diagnostico(db: Session, diagnostico_id: UUID):
    db.query(Diagnosticos).filter(Diagnosticos.id == diagnostico_id).delete()
    db.commit()


# ============================================================================
# PLAN DE TRATAMIENTO
# ============================================================================

def crear_plan_tratamiento(db: Session, data: PlanTratamientoCreate):
    db_obj = PlanTratamiento(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_plan_tratamiento(db: Session, historia_clinica_id: UUID):
    return db.query(PlanTratamiento).filter(
        PlanTratamiento.historia_clinica_id == historia_clinica_id
    ).first()


def actualizar_plan_tratamiento(db: Session, historia_clinica_id: UUID, data: PlanTratamientoCreate):
    plan = obtener_plan_tratamiento(db, historia_clinica_id)
    if plan:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(plan, key, value)
        db.commit()
        db.refresh(plan)
        return plan
    else:
        return crear_plan_tratamiento(db, data)


# ============================================================================
# REMISIONES A ESPECIALISTAS
# ============================================================================

def crear_remision(db: Session, data: RemisionesEspecialistasCreate):
    db_obj = RemisionesEspecialistas(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def obtener_remisiones(db: Session, historia_clinica_id: UUID):
    return db.query(RemisionesEspecialistas).filter(
        RemisionesEspecialistas.historia_clinica_id == historia_clinica_id
    ).all()


def obtener_remisiones_urgentes(db: Session, historia_clinica_id: UUID = None):
    query = db.query(RemisionesEspecialistas).filter(
        RemisionesEspecialistas.prioridad == "Urgente"
    )
    if historia_clinica_id:
        query = query.filter(RemisionesEspecialistas.historia_clinica_id == historia_clinica_id)
    return query.all()


def eliminar_remision(db: Session, remision_id: UUID):
    db.query(RemisionesEspecialistas).filter(RemisionesEspecialistas.id == remision_id).delete()
    db.commit()
