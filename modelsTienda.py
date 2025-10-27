from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class categoriaBase(BaseModel):
    name: str | None = Field(description="Nombre de la categoria")
    description: str | None = Field(description="Descripción de la categoria")

class categoria(categoriaBase, table=True):
    id: int | None = Field(default = None, primary_key = True)
