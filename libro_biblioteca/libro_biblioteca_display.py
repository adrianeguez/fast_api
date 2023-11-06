from datetime import datetime
from pydantic import BaseModel, Field
from libro_biblioteca.enums.genero_libro_enum import GeneroLibroEnum
class LibroBibliotecaDisplay(BaseModel):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime | None = None
    updated_at: datetime | None = None
    sis_habilitado:bool = False
    genero_libro: GeneroLibroEnum = GeneroLibroEnum.accion
    nombre: str = Field(min_length=3, max_length=40)
    description: str = Field(min_length=3, max_length=255, index=True)
    isbn: str =  Field(min_length=10, max_length=255)

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


