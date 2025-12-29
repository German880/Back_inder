from pydantic import BaseModel
from datetime import date
from uuid import UUID

class DeportistaCreate(BaseModel):
    documento: str
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    sexo: str

class DeportistaResponse(DeportistaCreate):
    id: UUID
