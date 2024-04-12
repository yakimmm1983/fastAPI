#NoteResponseDTO
from pydantic import BaseModel


class NoteResponseDTO(BaseModel):
    user_id:int
    note_name:str
    note_content:str