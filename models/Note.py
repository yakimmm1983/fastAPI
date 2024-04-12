from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, ForeignKey
from db_initialaizer import Base


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, nullable=False, primary_key=True)
    note_content = Column(String, nullable=False, unique=False)
    note_name = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    PrimaryKeyConstraint("id",name="notes_pkey")