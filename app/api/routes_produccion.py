from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.produccion import Produccion

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_produccion(data: dict, db: Session = Depends(get_db)):
    nuevo = Produccion(**data)
    db.add(nuevo)
    db.commit()
    return {"mensaje": "Producción registrada"}