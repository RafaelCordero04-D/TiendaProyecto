from TiendaDb import SessionDep
from fastapi import APIRouter, HTTPException, Query, status
from modelsTienda import producto, productoCreate, productoUpdate, categoria
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

router = APIRouter()

@router.post("/", response_model= producto, status_code=201 )
async def create_producto(new_producto: productoCreate, session: SessionDep):
    producto_data = new_producto.model_dump()
    if producto_data.get("stock", 0) < 0:
        raise HTTPException(status_code=400, detail="El stock no puede ser negativo.")
    categoria_db = session.get_one(categoria, producto_data.get("categoria_id"))
    if not categoria_db:
        raise HTTPException(status_code=400, detail="Categoria not found.")
    Producto = producto.model_validate(producto_data)
    session.add(Producto)
    session.commit()
    session.refresh(Producto)
    return Producto

@router.get("/productos", response_model=list[producto], status_code=200)
async def get_productos(session: SessionDep,
            stock: int |None = Query(None, description="Filtrar por stock exacto"),
            precio_min: float |None = Query(None, description="precio minimo"),
            precio_max: float |None =Query(None, description="precio maximo"),
            categoria_id: int |None = Query(None, description="Filtrar por ID de la categoria")
            ):
    query = session.query(producto).filter(producto.status == True)

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

@router.get("/productos/search", response_model=list[producto], status_code=200)
async def get_producto_by_categoria(nombre_categoria: str, session: SessionDep):
    categoria_stmt =select(categoria).where(categoria.name.ilike(f"%{nombre_categoria}%"))
    categoria_result = session.exec(categoria_stmt).first()

    if not categoria_result:
        raise HTTTPExeption(status_code=404, detail=f"No se encontro ninguna categoria con el nombre '{nombre_categoria}'.")

    productos_stmt = select(producto).where(producto.categoria_id == categoria_result.id)
    productos = session.exec(productos_stmt).all()

    if not productos:
        raise HTTPException(status_code= 404, detail=f"No hay productos registrados en la categoría '{categoria_result.nombre}'.")
    return productos

@router.get("/producto/ActiveOrInactive/", response_model=list[producto], status_code=200)
async def get_productos_by_status(its_active: bool, session: SessionDep):
    statement = select(producto).where(producto.status == its_active)
    results = session.exec(statement).all()
    if not results:
        raise HTTPException(status_code=404, detail="No Productos found with that status.")
    return results

@router.patch("/productoUpdate/{producto_id}", status_code=200)
async def update_producto(new_producto: productoUpdate, producto_id:int , session: SessionDep):
    producto_db = session.get(producto, producto_id)
    if not producto_db:
        raise HTTPException(status_code= 404, detail="Producto not found.")
    producto_update = new_producto.model_dump(exclude_unset=True)
    producto_db.sqlmodel_update(producto_update)
    session.add(producto_db)
    session.commit()
    session.refresh(producto_db)
    return producto_db

@router.delete("/productoDelete/{producto_id}", response_model=producto, status_code=200)
async def delete_producto(producto_id: int, session: SessionDep):
    producto_db = session.get(producto, producto_id)
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto not found.")
    if not producto_db.status:
        raise HTTPException(status_code=404, detail="Producto already inactive.")
    producto_db.status = False
    session.add(producto_db)
    session.commit()
    session.refresh(producto_db)
    return {"message": f"Producto'{producto_db.name}' has been desactivated"}

@router.put("/productoActivate/{producto_id}", response_model=producto, status_code=200)
async def activate_producto(producto_id: int, session: SessionDep):
    producto_db = session.get(producto, producto_id)
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto not found.")
    if producto_db.status:
        raise HTTPException(status_code=404, detail="Producto already activate.")
    producto_db.status = True
    session.add(producto_db)
    session.commit()
    session.refresh(producto_db)
    return {"message": f"Producto'{producto_db.name}' has been activated"}

@router.put("/producto/comprar/{producto_id}", response_model= producto, status_code = 200)
async def comprar_producto(producto_id: int, cantidad:int, session: SessionDep):
    producto_db = session.get(producto,producto_id)
    if not producto_db:
        raise HTTPException(status_code=404, detail="Producto not found.")
    if not producto_db.status:
        raise HTTPException(status_code=404, detail="El producto no esta activo y no se puede comprar.")
    if cantidad <= 0:
        raise HTTPException(status_code=404, detail="La cantidad debe ser mayor que cero.")
    if producto_db.stock < cantidad:
        raise HTTPException(status_code=404, detail=f"Stock insuficiente. Disponible: '{producto_db.stock}, solicitando: '{cantidad}'.'")

    producto_db.stock -= cantidad
    session.add(producto_db)
    session.commit()
    session.refresh(producto_db)
    return producto_db