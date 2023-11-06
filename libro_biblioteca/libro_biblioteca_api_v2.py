from datetime import datetime, date

from fastapi import Depends, APIRouter, status

from libro_biblioteca.dto.libro_biblioteca_create_dto import LibroBibliotecaCreateDto
from libro_biblioteca.dto.libro_biblioteca_update_dto import LibroBibliotecaUpdateDto
from libro_biblioteca.enums.genero_libro_enum import GeneroLibroEnum
from libro_biblioteca.libro_biblioteca_display import LibroBibliotecaDisplay
from libro_biblioteca.libro_biblioteca_model_v2 import LibroBibliotecaSchemaModel
from libro_biblioteca.libro_biblioteca_repository_v2 import LibroBibliotecaSqliteRepoV2
from libro_biblioteca.libro_biblioteca_schema import LibroBibliotecaSchema

name = "v2/libro-biblioteca"
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
        repo: LibroBibliotecaSqliteRepoV2 = Depends(LibroBibliotecaSqliteRepoV2)
        ) -> list[LibroBibliotecaDisplay]:
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

@router.get("/{id}", response_model=LibroBibliotecaDisplay, status_code=status.HTTP_200_OK)
def get_one(id: int,
            repo: LibroBibliotecaSqliteRepoV2 = Depends(LibroBibliotecaSqliteRepoV2)
            ) -> LibroBibliotecaDisplay:
    return repo.get_one(id)

@router.post("/", response_model=LibroBibliotecaDisplay, status_code=status.HTTP_201_CREATED)
def add(record: LibroBibliotecaCreateDto,
            repo: LibroBibliotecaSqliteRepoV2 = Depends(LibroBibliotecaSqliteRepoV2)
        ) -> LibroBibliotecaDisplay:
    return repo.add(record)


@router.patch("/{id}", response_model=LibroBibliotecaDisplay, status_code=status.HTTP_200_OK)
def update_one(id: int,
            record: LibroBibliotecaUpdateDto,
            repo: LibroBibliotecaSqliteRepoV2 = Depends(LibroBibliotecaSqliteRepoV2)
            ) -> LibroBibliotecaDisplay:
    return repo.update_one(id,record)


@router.delete("/{id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def update_one(id: int,
               repo: LibroBibliotecaSqliteRepoV2 = Depends(LibroBibliotecaSqliteRepoV2)
               ) -> None:
    return repo.delete_one(id)

