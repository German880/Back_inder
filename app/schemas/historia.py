from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class HistoriaCreate(BaseModel):
    deportista_id: UUID

class HistoriaResponse(BaseModel):
    id: UUID
    deportista_id: UUID
    fecha_apertura: datetime
