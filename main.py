from fastapi import FastAPI

import categoria
from TiendaDb import create_tables
app = FastAPI(lefespan = create_tables, tittle="Sistema de gestión de Tienda Online")
app.include_router(categoria.router, tags=["categoria"], prefix="/categoria")



