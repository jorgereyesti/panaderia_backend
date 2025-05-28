from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api import routes_registro, routes_produccion

from app.models import registro, produccion

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Panadería Social")

app.include_router(routes_registro.router, prefix="/registro", tags=["Registro"])
app.include_router(routes_produccion.router, prefix="/produccion", tags=["Producción"])