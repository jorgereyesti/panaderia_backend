from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class Produccion(Base):
    __tablename__ = "produccion"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    panificados = Column(String)
    cantidad = Column(Integer)