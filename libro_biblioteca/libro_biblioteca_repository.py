from abc import ABCMeta, abstractmethod
from typing import Optional, List
from datetime import datetime
from fastapi import HTTPException
from sqlalchemy import or_

from libro_biblioteca.dto.libro_biblioteca_create_dto import LibroBibliotecaCreateDto
from libro_biblioteca.dto.libro_biblioteca_update_dto import LibroBibliotecaUpdateDto
from libro_biblioteca.enums.genero_libro_enum import GeneroLibroEnum
from libro_biblioteca.libro_biblioteca_schema import LibroBibliotecaSchema
from sqlmodel import Session, select
from session.db_session import get_session, engine


# from fastapi import Depends

class LibroBibliotecaRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_one(self, id: int) -> Optional[LibroBibliotecaSchema]:
        pass

    @abstractmethod
    async def get(self) -> List[LibroBibliotecaSchema]:
        pass

    @abstractmethod
    async def add(self, user: LibroBibliotecaCreateDto) -> LibroBibliotecaSchema:
        pass

    @abstractmethod
    async def update_one(self, id: int, user: LibroBibliotecaUpdateDto) -> LibroBibliotecaSchema:
        pass

    @abstractmethod
    async def delete_one(self, id: int) -> None:
        pass


class LibroBibliotecaSqliteRepo(LibroBibliotecaRepo):
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
    ) -> list[LibroBibliotecaSchema]:
        with (Session(engine) as session):
            query = select(
                LibroBibliotecaSchema
            )
            if genero_libro:
                query = query.where(
                    LibroBibliotecaSchema.genero_libro == genero_libro
                )
            if created_at:
                query = query.where(
                    LibroBibliotecaSchema.created_at >= created_at
                )
            if updated_at:
                query = query.where(
                    LibroBibliotecaSchema.updated_at >= updated_at
                )
            if isbn:
                query = query.where(
                    LibroBibliotecaSchema.isbn == isbn
                )
            if nombre:
                query = query.where(
                    or_(LibroBibliotecaSchema.nombre == nombre)
                )
            if description:
                query = query.where(
                    or_(LibroBibliotecaSchema.description == description)
                )
            return session.exec(query.offset(offset).limit(limit)).all()

    def get_one(self, id: int) -> LibroBibliotecaSchema:
        with Session(engine) as session:
            record = session.get(LibroBibliotecaSchema, id)
            if not record:
                raise HTTPException(status_code=404, detail="Not found")
            return record

    def add(self, record: LibroBibliotecaCreateDto) -> LibroBibliotecaSchema:
        with Session(engine) as session:
            new_record = LibroBibliotecaSchema.from_orm(record)
            session.add(new_record)
            session.commit()
            session.refresh(new_record)
            return new_record

    def update_one(self, id: int, update_record: LibroBibliotecaUpdateDto) -> LibroBibliotecaSchema:
        with Session(engine) as session:
            record = session.get(LibroBibliotecaSchema, id)
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
                return record
            else:
                raise HTTPException(status_code=404, detail=f"No record with id={id}")

    def delete_one(self, id: int) -> None:
        with Session(engine) as session:
            record = session.get(LibroBibliotecaSchema, id)
            if record:
                session.delete(record)
                session.commit()
            else:
                raise HTTPException(status_code=404, detail=f"No car with id={id}.")