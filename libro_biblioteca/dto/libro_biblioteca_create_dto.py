from pydantic import Field

from libro_biblioteca.dto.libro_biblioteca_comun_dto import LibroBibliotecaComunDto, LibroBibliotecaConfig


class LibroBibliotecaCreateDto(LibroBibliotecaComunDto):
    isbn: str = Field(min_length=10, max_length=255)
    class Config:
        schema_extra = {
            "example": {
                **LibroBibliotecaConfig,
                "isbn": "isbn(10-255)"
            }
        }