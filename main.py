from fastapi import FastAPI
from sqlmodel import SQLModel
from TiendaDb import engine
import router_categoria
import router_producto
from TiendaDb import create_tables
app = FastAPI(lefespan = create_tables, tittle="Sistema de Gestión de Tienda Online")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
app.include_router(router_categoria.router, tags=["categoria"], prefix="/categoria")
app.include_router(router_producto.router, tags=["producto"], prefix="/producto")



