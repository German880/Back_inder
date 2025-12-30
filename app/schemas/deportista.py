from pydantic import BaseModel, field_validator
from datetime import date, datetime
from uuid import UUID

class DeportistaCreate(BaseModel):
    tipo_documento_id: str | UUID
    numero_documento: str
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    sexo_id: str | UUID
    telefono: str | None = None
    email: str | None = None
    direccion: str | None = None
    estado_id: str | UUID
    
    @field_validator('tipo_documento_id', 'sexo_id', 'estado_id', mode='before')
    @classmethod
    def validate_uuids(cls, v):
        if isinstance(v, UUID):
            return v
        if isinstance(v, str):
            try:
                return UUID(v)
            except ValueError:
                raise ValueError(f"Invalid UUID: {v}")
        raise ValueError(f"Expected UUID or string, got {type(v)}")

class DeportistaResponse(BaseModel):
    id: UUID
    tipo_documento_id: UUID
    numero_documento: str
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    sexo_id: UUID
    telefono: str | None = None
    email: str | None = None
    direccion: str | None = None
    estado_id: UUID
    created_at: datetime | None = None
    
    class Config:
        from_attributes = True
        extra = "ignore"  # Ignorar campos que no están en el schema
