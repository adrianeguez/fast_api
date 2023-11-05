from datetime import datetime

from sqlmodel import SQLModel, Field

from sqlalchemy_utils import ChoiceType
from libro_biblioteca.enums.genero_libro_enum import GeneroLibroEnum
from sqlalchemy import Column, TIMESTAMP, func, Boolean, Integer, String


class LibroBibliotecaSchema(SQLModel,table = True):
    __tablename__ = "libro_biblioteca"
    id: int | None = Field(default=None, primary_key=True, sa_column=Column(Integer, primary_key=True, index=True, autoincrement=True))
    created_at: datetime | None = Field(sa_column= Column(TIMESTAMP(timezone=True),
                                                   nullable=False, server_default=func.now()))
    updated_at: datetime | None = Field(sa_column=Column(TIMESTAMP(timezone=True),
                                                  default=None, onupdate=func.now()))
    sis_habilitado:bool = Field(sa_column= Column(Boolean, default=False))
    genero_libro: GeneroLibroEnum = Field(sa_column=Column(
        ChoiceType(GeneroLibroEnum, impl=String()),
        nullable=False,
        default=GeneroLibroEnum.accion,
    ))
    nombre: str = Field(min_length=3, max_length=40, sa_column= Column(String,index=True))
    description: str = Field(min_length=3, max_length=255)
    isbn: str =  Field(min_length=10, max_length=255, sa_column= Column(String, index=True, unique=True))

    class Config:
        schema_extra = {
            "example": {
                "id": 0,
                "created_at": "2023-11-04T23:38:02.789Z",
                "updated_at": "2023-11-04T23:38:02.789Z",
                "sis_habilitado": False,
                "genero_libro": "drama | accion | romantico ",
                "nombre": "string(3-40)",
                "description": "string(3-255)",
                "isbn": "stringstri(10-255)"
            }
        }

