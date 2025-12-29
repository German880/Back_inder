from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional

class CitaCreate(BaseModel):
    deportista_id: UUID
    fecha_inicio: datetime
    fecha_fin: datetime
    tipo: str
    observaciones: Optional[str] = None

class CitaResponse(CitaCreate):
    id: UUID
    estado: str
