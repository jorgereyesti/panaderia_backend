from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.db.base import Base

class Integrante(Base):
    __tablename__ = "integrantes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    dni = Column(String)
    fecha_nac = Column(Date)
    escolaridad = Column(String)
    vinculo = Column(String)
    condicion = Column(String)
    registro_id = Column(Integer, ForeignKey("registros.id"))