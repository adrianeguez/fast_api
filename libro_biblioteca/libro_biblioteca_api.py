from datetime import datetime, date

from fastapi import Depends, APIRouter, status

from libro_biblioteca.dto.libro_biblioteca_create_dto import LibroBibliotecaCreateDto
from libro_biblioteca.dto.libro_biblioteca_update_dto import LibroBibliotecaUpdateDto
from libro_biblioteca.enums.genero_libro_enum import GeneroLibroEnum
from libro_biblioteca.libro_biblioteca_repository import LibroBibliotecaSqliteRepo
from libro_biblioteca.libro_biblioteca_schema import LibroBibliotecaSchema

name = "libro-biblioteca"
router = APIRouter(prefix=f"/api/{name}", tags=[name])
tag_libro_biblioteca = {
    "name": name,
    "description": "Manage items. So _fancy_ they have their own docs.",
    "externalDocs": {
        "description": "Items external docs",
        "url": "https://fastapi.tiangolo.com/",
    },
}

@router.get("/", status_code=status.HTTP_200_OK)
def get(genero_libro: GeneroLibroEnum | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        nombre: str | None = None,
        description: str| None = None,
        isbn: str| None = None,
        offset: int | None = None,
        limit: int | None = None,
        repo: LibroBibliotecaSqliteRepo = Depends(LibroBibliotecaSqliteRepo)
        ) -> list[LibroBibliotecaSchema]:
    return repo.get(
        genero_libro=genero_libro,
        created_at=created_at,
        updated_at=updated_at,
        nombre=nombre,
        description=description,
        isbn=isbn,
        offset=offset,
        limit=limit,
    )

@router.get("/{id}", response_model=LibroBibliotecaSchema, status_code=status.HTTP_200_OK)
def get_one(id: int,
            repo: LibroBibliotecaSqliteRepo = Depends(LibroBibliotecaSqliteRepo)
            ) -> LibroBibliotecaSchema:
    return repo.get_one(id)

@router.post("/", response_model=LibroBibliotecaSchema, status_code=status.HTTP_201_CREATED)
def add(record: LibroBibliotecaCreateDto,
            repo: LibroBibliotecaSqliteRepo = Depends(LibroBibliotecaSqliteRepo)
        ) -> LibroBibliotecaSchema:
    return repo.add(record)


@router.patch("/{id}", response_model=LibroBibliotecaSchema, status_code=status.HTTP_200_OK)
def update_one(id: int,
            record: LibroBibliotecaUpdateDto,
            repo: LibroBibliotecaSqliteRepo = Depends(LibroBibliotecaSqliteRepo)
            ) -> LibroBibliotecaSchema:
    return repo.update_one(id,record)


@router.delete("/{id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def update_one(id: int,
               repo: LibroBibliotecaSqliteRepo = Depends(LibroBibliotecaSqliteRepo)
               ) -> None:
    return repo.delete_one(id)

