from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import uuid

class Cita(Base):
    __tablename__ = "citas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    deportista_id = Column(UUID(as_uuid=True), nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    tipo = Column(String, nullable=False)      # Ej: Evaluación, Control
    estado = Column(String, default="programada")  
    observaciones = Column(String)
