from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class categoriaBase(SQLModel):
    name: str | None = Field(description="Nombre de la categoria")
    description: str | None = Field(description="Descripción de la categoria")
    status: bool = Field(description="True= activate, False= deactivate", default = True)

class categoria(categoriaBase, table=True):
    id: int | None = Field(default = None, primary_key = True)
    productos: list["producto"] = Relationship(back_populates="categoria")

class categoriaCreate(categoriaBase):
    pass

class categoriaUpdate(categoriaBase):
    pass


class productoBase(SQLModel):
    name:str | None = Field(description="Nombre del producto")
    price:float | None = Field(description="Precio del producto")
    stock:int | None = Field(description="Stock del producto")
    description: str | None = Field(description="Descripcion del produto")
    status: bool | None = Field(description= "True= activate, False= deactivate", default = True)

class producto(productoBase, table=True):
    id: int | None = Field(default= None, primary_key= True)
    categoria_id: int = Field(foreign_key= "categoria.id")
    categoria: "categoria" = Relationship(back_populates="productos")

class productoCreate(productoBase):
    categoria_id: int = Field(foreign_key="categoria.id")

class productoUpdate(productoBase):
    pass


