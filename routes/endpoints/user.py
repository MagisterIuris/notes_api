from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from routes import router 
from schemas import UserDTO
from dependencies import get_user_service
from services import UserService


@router.post("/users")
def create_a_user (user: UserDTO, user_service: UserService = Depends(get_user_service)):
    user_service.create_user(user)
    return JSONResponse(
        status_code = 201, 
        content = {
            "detail" : "User successfully created !"
        }
    )
    
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends(get_user_service)): 
    token = user_service.authenticate_user(form_data.username, form_data.password)
    return {
            "access_token" : token, 
            "token_type" : "bearer"
        }