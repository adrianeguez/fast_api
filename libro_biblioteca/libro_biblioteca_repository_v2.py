from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Optional, List
from sqlalchemy import or_
from fastapi import Depends, HTTPException
from libro_biblioteca.dto.libro_biblioteca_create_dto import LibroBibliotecaCreateDto
from libro_biblioteca.dto.libro_biblioteca_update_dto import LibroBibliotecaUpdateDto
from libro_biblioteca.enums.genero_libro_enum import GeneroLibroEnum
from libro_biblioteca.libro_biblioteca_display import LibroBibliotecaDisplay
from libro_biblioteca.libro_biblioteca_model_v2 import LibroBibliotecaSchemaModel
from session.db_session import SessionLocal


# from fastapi import Depends

class LibroBibliotecaRepoV2:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_one(self, id: int) -> Optional[LibroBibliotecaDisplay]:
        pass

    @abstractmethod
    async def get(self) -> List[LibroBibliotecaDisplay]:
        pass

    @abstractmethod
    async def add(self, user: LibroBibliotecaCreateDto) -> LibroBibliotecaDisplay:
        pass

    @abstractmethod
    async def update_one(self, id: int, user: LibroBibliotecaUpdateDto) -> LibroBibliotecaDisplay:
        pass

    @abstractmethod
    async def delete_one(self, id: int) -> None:
        pass


class LibroBibliotecaSqliteRepoV2(LibroBibliotecaRepoV2):
    def get(
            self,
            genero_libro: GeneroLibroEnum | None = None,
            created_at: datetime| None= None,
            updated_at: datetime| None= None,
            nombre: str| None= None,
            description: str| None= None,
            isbn: str| None = None,
            offset: int | None = 0,
            limit: int | None = 10,
    ) -> list[LibroBibliotecaDisplay]:
        with (SessionLocal() as session):
            query = session.query(LibroBibliotecaSchemaModel)
            query_or = []
            if genero_libro:
                query = query.filter(
                    LibroBibliotecaSchemaModel.genero_libro == genero_libro
                )
            if created_at:
                query = query.filter(
                    LibroBibliotecaSchemaModel.created_at >= created_at
                )
            if updated_at:
                query = query.filter(
                    LibroBibliotecaSchemaModel.updated_at >= updated_at
                )
            if isbn:
                query = query.filter(
                    LibroBibliotecaSchemaModel.isbn == isbn
                )
            if nombre:
                query_or.append(LibroBibliotecaSchemaModel.nombre == nombre)
            if description:
                query_or.append(LibroBibliotecaSchemaModel.description.ilike(description))
            if len(query_or) > 0:
                query = query.filter(or_(*query_or))
            records = query.offset(offset).limit(limit).all()
            new_records = []
            for record in records:
                new_records.append(LibroBibliotecaDisplay(
                    id=record.id,
                    created_at=record.created_at,
                    updated_at=record.updated_at,
                    sis_habilitado=record.sis_habilitado,
                    genero_libro=record.genero_libro,
                    nombre=record.nombre,
                    description=record.description,
                    isbn=record.isbn
                ))
            return new_records

    def get_one(self, id: int) -> LibroBibliotecaDisplay:
        with SessionLocal() as session:
            record = session.get(LibroBibliotecaSchemaModel, id)
            if not record:
                raise HTTPException(status_code=404, detail="Not found")
            return record

    def add(self,
            record: LibroBibliotecaCreateDto) -> LibroBibliotecaDisplay:
        with SessionLocal() as session:
            new_record = LibroBibliotecaSchemaModel(
                id=None,
                created_at=None,
                updated_at=None,
                sis_habilitado=record.sis_habilitado,
                genero_libro=record.genero_libro,
                nombre=record.nombre,
                description=record.description,
                isbn=record.isbn
            )
            session.add(new_record)
            session.commit()
            session.refresh(new_record)
            return LibroBibliotecaDisplay(
                id=new_record.id,
                created_at=new_record.created_at,
                updated_at=new_record.updated_at,
                sis_habilitado=record.sis_habilitado,
                genero_libro=record.genero_libro,
                nombre=record.nombre,
                description=record.description,
                isbn=record.isbn
            )

    def update_one(self, id: int, update_record: LibroBibliotecaUpdateDto) -> LibroBibliotecaDisplay:
        with SessionLocal() as session:
            record = session.get(LibroBibliotecaSchemaModel, id)
            if record:
                if update_record.nombre:
                    record.nombre = update_record.nombre
                if update_record.sis_habilitado != None:
                    record.sis_habilitado = update_record.sis_habilitado
                if update_record.description:
                    record.description = update_record.description
                if update_record.genero_libro:
                    record.genero_libro = update_record.genero_libro
                session.commit()
                session.refresh(record)
                return LibroBibliotecaDisplay(
                    id=record.id,
                    created_at=record.created_at,
                    updated_at=record.updated_at,
                    sis_habilitado=record.sis_habilitado,
                    genero_libro=record.genero_libro,
                    nombre=record.nombre,
                    description=record.description,
                    isbn=record.isbn
                )
            else:
                raise HTTPException(status_code=404, detail=f"No record with id={id}")

    def delete_one(self, id: int) -> None:
        with SessionLocal() as session:
            record = session.get(LibroBibliotecaSchemaModel, id)
            if record:
                session.delete(record)
                session.commit()
            else:
                raise HTTPException(status_code=404, detail=f"No car with id={id}.")