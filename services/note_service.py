from repositories import NoteRepository
from schemas import NoteCreateDTO, NoteUpdateDTO
from domain import Note
from exceptions import NotFoundException

class NoteService: 
    def __init__(self, note_repository: NoteRepository): 
        self.note_repository = note_repository

    def get_notes(self, user_id: int): 
        return self.note_repository.get_notes(user_id)
    
    def create_note(self, user_id: int, note_info: NoteCreateDTO): 
        return self.note_repository.create_note(
            Note(
                title= note_info.title, 
                content= note_info.content, 
                user_id = user_id
            )
        )
    
    def update_note(self, note_id: int, user_id: int, note_info: NoteUpdateDTO): 
        note = self.note_repository.get_note(note_id, user_id)
        content = note_info.content
        title = note_info.title
        if not note: 
            raise NotFoundException("Not found.")        
        if content is not None: 
            note.content = content 
        if title is not None: 
            note.title = title 

        return self.note_repository.save_note(note)
    

    def delete_note(self, note_id: int, user_id: int): 
        note = self.note_repository.get_note(note_id, user_id)
        if not note: 
            raise NotFoundException("Note not found.")
        self.note_repository.delete_note(note)
        

        






    