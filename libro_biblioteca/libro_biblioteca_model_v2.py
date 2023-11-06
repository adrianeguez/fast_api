from datetime import datetime

from sqlalchemy_utils import ChoiceType
from libro_biblioteca.enums.genero_libro_enum import GeneroLibroEnum
from sqlalchemy import Column, TIMESTAMP, func, Boolean, Integer, String

from session.db_session import Base


class LibroBibliotecaSchemaModel(Base):
    __tablename__ = "libro_biblioteca"
    id: int | None = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at: datetime | None = Column(TIMESTAMP(timezone=True),
                                         nullable=False, server_default=func.now())
    updated_at: datetime | None = Column(TIMESTAMP(timezone=True),
                                         default=None, onupdate=func.now())
    sis_habilitado:bool = Column(Boolean, default=False)
    genero_libro: GeneroLibroEnum = Column(
        ChoiceType(GeneroLibroEnum, impl=String()),
        nullable=False,
        default=GeneroLibroEnum.accion,
    )
    nombre: str = Column(String,index=True)
    description: str = Column(String,index=True)
    isbn: str =  Column(String, index=True, unique=True)


