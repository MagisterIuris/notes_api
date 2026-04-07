from domain import User
from schemas import UserDTO
from repositories import UserRepository
from exceptions import WrongPasswordException, EmailNotFoundException, PasswordTooShortException, InvalidEmailFormatException
from services import AuthService
from sqlalchemy.exc import NoResultFound


class UserService : 
    def __init__(self, user_repository: UserRepository, auth_service: AuthService): 
        self.user_repository = user_repository
        self.auth_service = auth_service

    def create_user(self, user):
        email, password = user.email, user.password
        print(email, password)
        self.user_repository.add_user(User(email=email, password_hash=self.auth_service.hash_password(password)))

    def authenticate_user(self, email, password): 
        self.verify_email_format(email)
        self.verify_password_length(password)
        
        try: 
            user_db = self.user_repository.find_user_by_email(str(email))
        except NoResultFound: 
            raise EmailNotFoundException("Email does not exist !")
        else : 
            if self.auth_service.compare_secrets(password, user_db.password_hash):  
                token = self.auth_service.create_access_token(user_db.id)
                return token 
            else: 
                raise WrongPasswordException("Wrong password !")      

    def verify_password_length(self, password: str):
        password_length = len(password)
        if not (8 <= password_length <= 72):
            raise PasswordTooShortException("Password should be between 8 and 72 characters.")
        
    def verify_email_format(self, email: str): 
        email_parts = email.split("@")
        if len(email_parts) != 2: 
            raise InvalidEmailFormatException("Email should contain the '@' symbol")
        
        domain_part = email_parts[1].split('.')
        if len(domain_part) != 2: 
            raise InvalidEmailFormatException("Domain part should contain the dot (for eg .com, .fr)")

