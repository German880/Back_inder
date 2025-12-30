from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, List

# ============================================================================
# ANTECEDENTE MÉDICO
# ============================================================================

class AntecedenteMedicoBase(BaseModel):
    codigoCIE11: str
    nombreEnfermedad: str
    observaciones: Optional[str] = None

class AntecedenteMedicoCreate(AntecedenteMedicoBase):
    pass

# ============================================================================
# ANTECEDENTE FAMILIAR
# ============================================================================

class AntecedenteFamiliarBase(BaseModel):
    codigoCIE11: str
    nombreEnfermedad: str
    familiar: str
    observaciones: Optional[str] = None

class AntecedenteFamiliarCreate(AntecedenteFamiliarBase):
    pass

# ============================================================================
# REVISIÓN POR SISTEMAS
# ============================================================================

class SistemaRevisionBase(BaseModel):
    estado: Optional[str] = None  # "normal" o "anormal"
    observaciones: Optional[str] = None

class RevisionSistemasCreate(BaseModel):
    cardiovascular: SistemaRevisionBase
    respiratorio: SistemaRevisionBase
    digestivo: SistemaRevisionBase
    neurologico: SistemaRevisionBase
    musculoesqueletico: SistemaRevisionBase
    genitourinario: SistemaRevisionBase
    endocrino: SistemaRevisionBase
    pielFaneras: SistemaRevisionBase

# ============================================================================
# EXPLORACIÓN FÍSICA
# ============================================================================

class SistemaExploracionBase(BaseModel):
    estado: Optional[str] = None  # "normal" o "anormal"
    observaciones: Optional[str] = None

class ExploracionSistemasCreate(BaseModel):
    cardiovascular: SistemaExploracionBase
    respiratorio: SistemaExploracionBase
    digestivo: SistemaExploracionBase
    neurologico: SistemaExploracionBase
    musculoesqueletico: SistemaExploracionBase
    genitourinario: SistemaExploracionBase
    endocrino: SistemaExploracionBase
    pielFaneras: SistemaExploracionBase

# ============================================================================
# PRUEBAS COMPLEMENTARIAS
# ============================================================================

class AyudaDiagnosticaBase(BaseModel):
    categoria: str  # "Laboratorios", "Imágenes", "Pruebas Funcionales"
    nombrePrueba: str
    codigoCUPS: str
    resultado: Optional[str] = None

class AyudaDiagnosticaCreate(AyudaDiagnosticaBase):
    pass

# ============================================================================
# DIAGNÓSTICO
# ============================================================================

class DiagnosticoCinicoBase(BaseModel):
    codigoCIE11: str
    nombreEnfermedad: str
    observaciones: Optional[str] = None

class DiagnosticoCinicoCreate(DiagnosticoCinicoBase):
    pass

# ============================================================================
# REMISIÓN ESPECIALISTA
# ============================================================================

class RemisionEspecialistaBase(BaseModel):
    especialista: str
    motivo: str
    prioridad: str  # "Normal" o "Urgente"
    fechaRemision: str

class RemisionEspecialistaCreate(RemisionEspecialistaBase):
    pass

# ============================================================================
# HISTORIA CLÍNICA BÁSICA
# ============================================================================

class HistoriaCreate(BaseModel):
    """Crear una historia clínica básica"""
    deportista_id: UUID
    
    class Config:
        from_attributes = True

# ============================================================================
# HISTORIA CLÍNICA COMPLETA
# ============================================================================

class HistoriaClinicaCompleteCreate(BaseModel):
    """Datos completos de una historia clínica con 7 pasos"""
    deportista_id: UUID
    
    # Paso 1: Evaluación
    tipoCita: str
    motivoConsulta: str
    enfermedadActual: str
    
    # Paso 2: Antecedentes Médicos
    antecedentesPersonales: List[AntecedenteMedicoCreate]
    antecedentesFamiliares: List[AntecedenteFamiliarCreate]
    lesionesDeportivas: bool = False
    descripcionLesiones: Optional[str] = None
    fechaUltimaLesion: Optional[str] = None
    cirugiasPrevias: bool = False
    detalleCirugias: Optional[str] = None
    tieneAlergias: bool = False
    alergias: Optional[str] = None
    tomaMedicacion: bool = False
    medicacionActual: Optional[str] = None
    vacunas: List[str] = []
    
    # Paso 3: Revisión por Sistemas
    revisionSistemas: RevisionSistemasCreate
    
    # Paso 4: Exploración Física
    estatura: Optional[str] = None
    peso: Optional[str] = None
    frecuenciaCardiaca: Optional[str] = None
    presionArterial: Optional[str] = None
    frecuenciaRespiratoria: Optional[str] = None
    temperatura: Optional[str] = None
    saturacionOxigeno: Optional[str] = None
    exploracionSistemas: ExploracionSistemasCreate
    
    # Paso 5: Pruebas Complementarias
    ayudasDiagnosticas: List[AyudaDiagnosticaCreate] = []
    
    # Paso 6: Diagnóstico
    analisisObjetivo: Optional[str] = None
    impresionDiagnostica: Optional[str] = None
    diagnosticosClinicos: List[DiagnosticoCinicoCreate] = []
    
    # Paso 7: Plan de Tratamiento
    indicacionesMedicas: Optional[str] = None
    recomendacionesEntrenamiento: Optional[str] = None
    planSeguimiento: Optional[str] = None
    remisionesEspecialistas: List[RemisionEspecialistaCreate] = []

# ============================================================================
# RESPUESTAS
# ============================================================================

class HistoriaResponse(BaseModel):
    id: UUID
    deportista_id: UUID
    fecha_apertura: datetime
    
    class Config:
        from_attributes = True
