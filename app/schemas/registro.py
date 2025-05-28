from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Integrante(BaseModel):
    nombre: str
    dni: str
    fecha_nac: date
    escolaridad: str
    vinculo: str
    condicion: str

class RegistroCreate(BaseModel):
    fecha_relevamiento: date
    cic: str
    nombre: str
    dni: str
    telefono: str
    direccion: str
    lena_social: str
    actividades_cic: str
    ingresos_formales: str
    huerta: str
    mantenimiento_economico: str
    observaciones: Optional[str] = None
    integrantes: List[Integrante]