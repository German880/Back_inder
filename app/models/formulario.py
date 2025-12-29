from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class RespuestaGrupo(Base):
    __tablename__ = "respuesta_grupos"

    id = Column(Integer, primary_key=True, index=True)
    historia_clinica_id = Column(Integer, nullable=False)
    formulario_id = Column(Integer, nullable=False)

    respuestas = relationship("RespuestaFormulario", back_populates="grupo")


class RespuestaFormulario(Base):
    __tablename__ = "respuesta_formulario"

    id = Column(Integer, primary_key=True, index=True)
    grupo_id = Column(Integer, ForeignKey("respuesta_grupos.id"))
    campo = Column(String, nullable=False)
    valor = Column(String, nullable=False)

    grupo = relationship("RespuestaGrupo", back_populates="respuestas")
