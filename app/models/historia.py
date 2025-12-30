from sqlalchemy import Column, Date, DateTime, ForeignKey, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime
import uuid

class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    deportista_id = Column(UUID(as_uuid=True), ForeignKey("deportistas.id"), nullable=False)
    fecha_apertura = Column(Date, nullable=False)
    estado_id = Column(UUID(as_uuid=True), ForeignKey("catalogo_items.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    deportista = relationship("Deportista", back_populates="historias")
    estado = relationship("CatalogoItem")
    archivos = relationship("ArchivoClinico", back_populates="historia_clinica")
    grupos = relationship("RespuestaGrupo", back_populates="historia_clinica")

class HistoriaClinicaJSON(Base):
    """Modelo para almacenar la historia clínica completa como JSON"""
    __tablename__ = "historias_clinicas_json"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    historia_clinica_id = Column(UUID(as_uuid=True), ForeignKey("historias_clinicas.id"), nullable=False)
    deportista_id = Column(UUID(as_uuid=True), ForeignKey("deportistas.id"), nullable=False)
    datos_completos = Column(JSON, nullable=False)  # JSON con todos los datos
    created_at = Column(DateTime, default=datetime.utcnow)