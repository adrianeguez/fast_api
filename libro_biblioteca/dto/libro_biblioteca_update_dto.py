from pydantic import Field, BaseModel

from libro_biblioteca.dto.libro_biblioteca_comun_dto import LibroBibliotecaComunDto, LibroBibliotecaConfig
from libro_biblioteca.enums.genero_libro_enum import GeneroLibroEnum


class LibroBibliotecaUpdateDto(BaseModel):
    sis_habilitado:bool | None
    genero_libro: GeneroLibroEnum | None
    nombre: str | None = Field(min_length=3, max_length=40)
    description: str | None =  Field(min_length=3, max_length=255)
    class Config():
        schema_extra = {
            "example": {
                **LibroBibliotecaConfig,
            }
        }

