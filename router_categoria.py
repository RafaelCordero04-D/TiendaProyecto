from TiendaDb import SessionDep
from fastapi import APIRouter, HTTPException
from modelsTienda import categoria, categoriaCreate, categoriaUpdate
from sqlalchemy.exc import IntegrityError
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

@router.get("/categorias", response_model=list[categoria])
async def get_all_categorias(session: SessionDep):
    categorias = session.query(categoria).all()
    return categorias

