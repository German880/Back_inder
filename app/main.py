from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import Base, engine   # ✅ CORRECTO

# Registrar modelos
from app.models import *

# Routers
from app.api.v1 import deportistas, historias, citas, archivos, cie11, cups, catalogos, antecedentes, historia_completa, historias_completa, documentos

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="Backend Historia Clínica Deportiva - INDER"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "environment": settings.APP_ENV
    }

app.include_router(deportistas.router, prefix="/api/v1/deportistas")
app.include_router(historias.router, prefix="/api/v1/historias_clinicas")
app.include_router(historia_completa.router, prefix="/api/v1")
app.include_router(historias_completa.router)
app.include_router(citas.router, prefix="/api/v1/citas")
app.include_router(archivos.router, prefix="/api/v1/archivos")
app.include_router(cie11.router, prefix="/api/v1/cie11")
app.include_router(cups.router, prefix="/api/v1/cups")
app.include_router(catalogos.router, prefix="/api/v1/catalogos")
app.include_router(antecedentes.router, prefix="/api/v1")
app.include_router(documentos.router, prefix="/api/v1")
