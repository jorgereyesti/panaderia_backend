from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class Registro(Base):
    __tablename__ = "registros"
    id = Column(Integer, primary_key=True, index=True)
    fecha_relevamiento = Column(Date)
    cic = Column(String)
    nombre = Column(String)
    dni = Column(String)
    telefono = Column(String)
    direccion = Column(String)