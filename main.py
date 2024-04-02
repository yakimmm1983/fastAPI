from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from DTO.request.User_request_DTO import User_request_DTO
from service import auth
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)
@app.post("/auth")
async def auth_user(user:User_request_DTO):
    return auth(user)
