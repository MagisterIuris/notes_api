from config import pwd_context, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta 
from jose import jwt 
from jose.exceptions import JWTError
from exceptions import InvalidTokenException


class AuthService: 
    def hash_password(self, password: str): 
        return pwd_context.hash(password)
    
    def compare_secrets(self, password: str, hash: str): 
        return pwd_context.verify(password, hash)
    
    def create_access_token(self, user_id: int):
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        }

        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )

        return token

    def decode_token(self, token: str): 
        try:    
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError: 
            raise InvalidTokenException("Your token is invalid !")
        
        user_id = payload.get("user_id")
        if user_id is None: 
            raise InvalidTokenException("Payload error.")
        
        return user_id