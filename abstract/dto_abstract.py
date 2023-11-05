from pydantic import BaseModel, Field
class DtoAbstract(BaseModel):
    sis_habilitado:bool | None = Field(default=True)