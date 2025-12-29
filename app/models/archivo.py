from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from datetime import datetime
import uuid

class ArchivoClinico(Base):
    __tablename__ = "archivos_clinicos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    historia_id = Column(UUID(as_uuid=True), nullable=False)
    nombre_original = Column(String, nullable=False)
    tipo_archivo = Column(String, nullable=False)  # pdf, jpg, png, dcm
    categoria = Column(String)  # laboratorio, imagen, prueba_funcional, deportiva
    ruta = Column(String, nullable=False)
    fecha_subida = Column(DateTime, default=datetime.utcnow)
