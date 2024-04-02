from pydantic import BaseModel
class User_request_DTO(BaseModel):
    username:str
    password:str