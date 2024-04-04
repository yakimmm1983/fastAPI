import bcrypt
import jwt
from sqlalchemy import Column,String,Integer,LargeBinary,Boolean,UniqueConstraint,PrimaryKeyConstraint
from db_initialaizer import Base

class User(Base):
    @staticmethod
    def hash_password(password) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    def validate_password(self,password) -> bool:
        return bcrypt.checkpw(password.encode(),self.hashed_password)
    def generate_token(self) -> dict:
        return {
            "access_token":jwt.encode(
                {"fullname":self.full_name,"login":self.login},
                "Secret_Key"
            )
        }

    __tablename__ = "users"
    login = Column(String(225), nullable=False, unique=False)
    id = Column(Integer, nullable=False, primary_key=True)
    hashed_password = Column(LargeBinary,nullable=False)
    full_name = Column(String(225),nullable=False)
    is_active = Column(Boolean,default = False)

    UniqueConstraint("login",name="uq_user_login")
    PrimaryKeyConstraint("id",name="pk_user_id")
    def __repr__(self):
        return "<User{full_name!r}>".format(full_name=self.full_name)

