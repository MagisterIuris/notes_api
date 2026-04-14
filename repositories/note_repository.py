from sqlalchemy.orm import Session
from domain import Note

class NoteRepository: 
    def __init__(self, db: Session): 
        self.db = db

    def get_notes(self, user_id: int): 
        return self.db.query(Note).filter(
                Note.user_id == user_id
            ).order_by(Note.id).all()
    
    def create_note(self, note: Note): 
        self.db.add(note)
        self.db.commit()
        self.db.refresh(note)
        return note 
    
    def get_note(self, note_id: int, user_id: int):
        return self.db.query(Note).filter(
                Note.id == note_id, 
                Note.user_id == user_id
            ).one_or_none()
    
    def save_note(self, note: Note): 
        self.db.commit()
        self.db.refresh(note)
        return note 
    

    def delete_note(self, note: Note): 
        self.db.delete(note)
        self.db.commit()