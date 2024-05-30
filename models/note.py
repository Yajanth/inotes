from pydantic import BaseModel


class User(BaseModel):
    title: str
    Desc : str
    Important : bool
