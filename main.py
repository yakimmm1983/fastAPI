from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from DTO.request.User_request_DTO import User_request_DTO
from sqlalchemy.orm import Session
from starlette import status

from DTO.response.User_response_DTO import CreateUserSchema
from models import User
from services import user_service
from db_initialaizer import get_db

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)
@app.post("/auth")
async def auth_user(
        user_request:User_request_DTO,
        session: Session = Depends(get_db)):
    try:
        user: User.User = user_service.get_user(
            session=session,login=user_request.username
        )
    except Exception:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid user credetionals"
        )
    is_valid:bool = user.validate_password(user_request.password)
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credetionals"
        )
    return user.generate_token()
@app.post('/signup')
def siginup(
        user_request: CreateUserSchema = Body(),
        session: Session = Depends(get_db)
):
    user_request.hashed_password = User.User.hash_password(user_request.hashed_password)
    return user_service.create_user(session,user=user_request)