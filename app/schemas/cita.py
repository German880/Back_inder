from pydantic import BaseModel
from datetime import date, time
from uuid import UUID
from typing import Optional

class CitaCreate(BaseModel):
    deportista_id: str  # UUID como string
    fecha: str  # YYYY-MM-DD
    hora: str  # HH:MM:SS
    tipo_cita_id: str  # UUID como string
    estado_cita_id: str  # UUID como string
    observaciones: Optional[str] = None

    class Config:
        from_attributes = True

class CitaUpdate(BaseModel):
    fecha: Optional[str] = None
    hora: Optional[str] = None
    tipo_cita_id: Optional[str] = None
    estado_cita_id: Optional[str] = None
    observaciones: Optional[str] = None

    class Config:
        from_attributes = True

class CitaResponse(BaseModel):
    id: str
    deportista_id: str
    fecha: str
    hora: str
    tipo_cita_id: str
    estado_cita_id: str
    observaciones: Optional[str]
    created_at: Optional[str]

    class Config:
        from_attributes = True
