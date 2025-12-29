from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from datetime import datetime
import uuid

class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    deportista_id = Column(UUID(as_uuid=True), ForeignKey("deportistas.id"))
    fecha_apertura = Column(DateTime, default=datetime.utcnow)
