from TiendaDb import SessionDep
from fastapi import APIRouter, HTTPException, Query, status
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

@router.get("/productos", response_model=list[producto], status_code=200)
async def get_all_productos(session: SessionDep,
            stock: int |None = Query(None, description="Filtrar por stock exacto"),
            precio_min: float |None = Query(None, description="precio minimo"),
            precio_max: float |None =Query(None, description="precio maximo"),
            categoria_id: int |None = Query(None, description="Filtrar por ID de la categoria")
            ):
    query = session.query(producto)

    if stock is not None:
        query = query.filter(producto.stock == stock)
    if precio_min is not None:
        query = query.filter(producto.price >= precio_min)
    if precio_max is not None:
        query = query.filter(producto.price <= precio_max)
    if categoria_id is not None:
        query= query.filter(producto.categoria_id == categoria_id)

    productos = query.all()

    if not productos:
        raise HTTPException(status_code=404, detail="No se encontraron productos con los filtros especificados.")
    return productos
