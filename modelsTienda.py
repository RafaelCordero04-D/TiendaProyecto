from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class categoriaBase(BaseModel):
    name: str | None = Field(description="Nombre de la categoria")
    description: str | None = Field(description="Descripción de la categoria")
