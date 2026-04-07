from routes import router 
from fastapi import Depends
from dependencies import get_current_user_id, get_note_service
from services import NoteService
from schemas import NoteDTO, NoteCreateDTO, NoteUpdateDTO


@router.get("/notes")
def get_authenticated_user_notes (user_id: int = Depends(get_current_user_id), 
                                  note_service: NoteService = Depends(get_note_service)): 
    notes = note_service.get_notes(user_id)
    return [NoteDTO.model_validate(note) for note in notes]


@router.post("/notes")
def create_user_note (note_info: NoteCreateDTO, 
                      user_id: int = Depends(get_current_user_id), 
                      note_service: NoteService = Depends(get_note_service)): 
    note = note_service.create_note(user_id, note_info)
    return NoteDTO.model_validate(note)


@router.patch("/notes/{id}")
def update_user_note (id: int, note_info: NoteUpdateDTO, 
                      user_id: int = Depends(get_current_user_id), 
                      note_service : NoteService = Depends(get_note_service)): 
    note = note_service.update_note(id, user_id, note_info)
    return NoteDTO.model_validate(note)
    

