from sqlalchemy.orm import Session
from models.Note import Note
from DTO.response.NoteResponnseDTO import NoteResponseDTO

def get_note_by_id(session:Session,id: int):
    return session.query(Note).filter(Note.id == id).one()
def get_notes_by_user_id(session:Session,user_id:int):
    return session.query(Note).filter(Note.user_id == user_id).all()
def create_note(session: Session,note:NoteResponseDTO ):
    db_note = Note(**note.dict())
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note