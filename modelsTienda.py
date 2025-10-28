from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class categoriaBase(BaseModel):
    name: str | None = Field(description="Nombre de la categoria")
    description: str | None = Field(description="Descripción de la categoria")

class categoria(categoriaBase, table=True):
    id: int | None = Field(default = None, primary_key = True)
    productos: list["producto"] = Relationship(back_populates="categoria")

class categoriaCreate(categoriaBase):
    pass

class categoriaUpdate(categoriaBase):
    pass


class productoBase(BaseModel):
    name:str | None = Field(description="Nombre del producto")
    price:float | None = Field(description="Precio del producto")
    stock:int | None = Field(description="Stock del producto")
    description: str | None = Fiel(dedscription="Descripcion del produto")

class producto(productoBase, table=True):
    id: int | None = Field(default= None, primary_key= True)
    categoria_id: int = Field(foreign_key= "categoria.id")
    categoria: Categoria = Relationship(back_populates="productos")

class productoCreate(productoBase):
    class spiderManCreate(spiderManBase):
        universe_id: int = Field(foreign_key="universe.id")

class productoUpdate(productoBase):
    pass


