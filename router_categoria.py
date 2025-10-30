from TiendaDb import SessionDep
from fastapi import APIRouter, HTTPException
from modelsTienda import categoria, categoriaCreate, categoriaUpdate
from sqlalchemy.exc import IntegrityError
from sqlmodel import select
router = APIRouter()

@router.post("/", response_model=categoria, status_code = 201)
async def create_categoria(new_categoria: categoriaCreate, session: SessionDep):
    Categoria = categoria.model_validate(new_categoria)
    session.add(Categoria)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=400, detail="El nombre de la categoria ya existe.")
    session.refresh(Categoria)
    return Categoria

@router.get("/categorias", response_model=list[categoria], status_code=200)
async def get_all_categorias(session: SessionDep):
    categorias = session.query(categoria).all()
    return categorias

@router.delete("/inactivate/{categoria_id}", response_model=categoria, status_code=200)
async def kill_one_categoria(categoria_id: int, session: SessionDep):
    categoria_db = session.get(categoria, categoria_id)
    if not categoria_db:
        raise HTTPException(status_code=404, detail="Categoria not found")
    if not categoria_db.status:
        raise HTTPException(status_code=404, detail="Categoria already inactive")
    categoria_db.status = False
    session.add(categoria_db)
    session.commit()
    session.refresh(categoria_db)
    return{"message": f"Categoria'{categoria_db.name}' has been desactivated"}

@router.get("/activateCategorias/", response_model=list[categoria], status_code=200)
async def get_categorias_by_status(session: SessionDep):
    statement = select(categoria).where(categoria.status == True)
    results = session.exec(statement).all()
    if not results:
        raise HTTPException(status_code=404, detail="No categorias found")
    return results

@router.patch("/categoriaUpdate/{categoria_id}", status_code=200)
async def update_categoria(new_categoria: categoriaUpdate, categoria_id: int, session: SessionDep ):
    categoria_db = session.get(categoria, categoria_id)
    if not categoria_db:
        raise HTTPException(status_code=404, detail="categoria not found")
    categoria_update = new_categoria.model_dump(exclude_unset=True)
    categoria_db.sqlmodel_update(categoria_update)
    session.add(categoria_db)
    session.commit()
    session.refresh(categoria_db)
    return categoria_db

