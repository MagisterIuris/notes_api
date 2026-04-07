from .authentication_exception import AuthenticationException

class WrongPasswordException(AuthenticationException): 
    pass