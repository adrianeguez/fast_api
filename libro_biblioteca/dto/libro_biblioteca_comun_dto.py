from pydantic import Field

from abstract.dto_abstract import DtoAbstract
from libro_biblioteca.enums.genero_libro_enum import GeneroLibroEnum


class LibroBibliotecaComunDto(DtoAbstract):
    genero_libro: GeneroLibroEnum = Field(GeneroLibroEnum.drama)
    nombre: str = Field(min_length=3, max_length=40)
    description: str =  Field(min_length=3, max_length=255)

LibroBibliotecaConfig = {
    "sis_habilitado": True,
    "genero_libro": "drama | accion | romantico ",
    "nombre": "string(3-40)",
    "description": "string(3-255)"
}
