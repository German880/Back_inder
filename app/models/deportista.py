from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import uuid

class Deportista(Base):
    __tablename__ = "deportistas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    documento = Column(String, unique=True, nullable=False)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    fecha_nacimiento = Column(Date)
    sexo = Column(String)
