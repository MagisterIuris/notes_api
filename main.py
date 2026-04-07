from routes import router as user_router
from database import Base, engine
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from exceptions import AuthenticationException, ValidationException, NotFoundException


app = FastAPI(title="Notes API", 
              description="Secure REST API with JWT authentication", 
              version="1.0.0")

app.include_router(user_router)
Base.metadata.create_all(bind=engine)


@app.exception_handler(AuthenticationException)
def handler (req: Request, exc: AuthenticationException): 
    return JSONResponse (
        status_code=401, 
        content={
            "detail" : exc.message
        }
    )


@app.exception_handler(ValidationException)
def handler(req: Request, exc: ValidationException): 
    return JSONResponse(
        status_code= 422, 
        content= {
            "detail": exc.message
        }
    )



@app.exception_handler(NotFoundException)
def handler(req: Request, exc: NotFoundException): 
    return JSONResponse(
        status_code= 404, 
        content= {
            "detail": exc.message
        }
    )
