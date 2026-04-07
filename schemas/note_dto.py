from pydantic import BaseModel
from datetime import datetime 

class NoteDTO (BaseModel): 
    id: int 
    title: str
    content: str 
    created_at: datetime

    model_config = {"from_attributes" : True}