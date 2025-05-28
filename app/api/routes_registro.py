from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.registro import Registro
from app.models.integrante import Integrante as IntegranteModel
from app.schemas.registro import RegistroCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_registro(data: RegistroCreate, db: Session = Depends(get_db)):
    nuevo = Registro(
        fecha_relevamiento=data.fecha_relevamiento,
        cic=data.cic,
        nombre=data.nombre,
        dni=data.dni,
        telefono=data.telefono,
        direccion=data.direccion,
        lena_social=data.lena_social,
        actividades_cic=data.actividades_cic,
        ingresos_formales=data.ingresos_formales,
        huerta=data.huerta,
        mantenimiento_economico=data.mantenimiento_economico,
        observaciones=data.observaciones
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    
    for i in data.integrantes:
        integrante = IntegranteModel(
            nombre=i.nombre,
            dni=i.dni,
            fecha_nac=i.fecha_nac,
            escolaridad=i.escolaridad,
            vinculo=i.vinculo,
            condicion=i.condicion,
            registro_id=nuevo.id
        )
        db.add(integrante)
    db.commit()

    return {"mensaje": "Formulario recibido correctamente"}