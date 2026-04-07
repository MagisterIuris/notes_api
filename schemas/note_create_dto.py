from pydantic import BaseModel

class NoteCreateDTO(BaseModel): 
    title: str
    content: str 