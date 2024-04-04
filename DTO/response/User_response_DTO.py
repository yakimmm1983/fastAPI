from pydantic import BaseModel, Field

class UserBase(BaseModel):
    login:str
    full_name:str
class UserSchema(UserBase):
    id:int
    is_active:bool = Field(default=False)

    class Config:
        orm_mode=True
class CreateUserSchema(UserBase):
    hashed_password:str = Field(alias = "password")
