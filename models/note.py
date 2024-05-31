from pydantic import BaseModel


class Note(BaseModel):
    title: str
    Desc : str
    Important : bool | None= None
