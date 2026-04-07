from fastapi import Depends 
from services import AuthService, UserService, NoteService
from repositories import UserRepository, NoteRepository
from database import SessionLocal 
from sqlalchemy.orm import Session
from config import oauth2_scheme


def get_auth_service(): 
    return AuthService()

def get_db(): 
    db = SessionLocal()
    try: 
        yield db 
    finally: 
        db.close()

def get_user_repository(db: Session = Depends(get_db)): 
    return UserRepository(db)

def get_note_repository(db: Session = Depends(get_db)): 
    return NoteRepository(db)

def get_user_service(user_repository: UserRepository = Depends(get_user_repository), auth_service: AuthService = Depends(get_auth_service)): 
    return UserService(user_repository, auth_service)

def get_note_service(note_repository: NoteRepository = Depends(get_note_repository)): 
    return NoteService(note_repository)

def get_current_user_id(token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends(get_auth_service)): 
    return auth_service.decode_token(token)
