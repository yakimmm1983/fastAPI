from fastapi import HTTPException
from starlette import status
from DTO.request.User_request_DTO import User_request_DTO
def auth(user:User_request_DTO):
    if user.username == "admin" and user.password == "qwerty":
        return
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user data"
        )