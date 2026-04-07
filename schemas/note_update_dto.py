from pydantic import BaseModel 

class NoteUpdateDTO(BaseModel): 
    title: str | None = None 
    content : str | None = None 