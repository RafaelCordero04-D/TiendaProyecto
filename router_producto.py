from TiendaDb import SessionDep
from fastapi import APIRouter, HTTPException
from modelsTienda import producto, productoCreate, productoUpdate, categoria
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

router = APIRouter()

@router.post("/", response_model= producto, status_code=201 )
async def create_producto(new_producto: productoCreate, session: SessionDep):
    producto_data = new_producto.model_dump()
    categoria_db = session.get_one(categoria, producto_data.get("categoria_id"))
    if not categoria_db:
        raise HTTPException(status_code=400, detail="Categoria not found.")
    Producto = producto.model_validate(producto_data)
    session.add(Producto)
    session.commit()
    session.refresh(Producto)
    return Producto

