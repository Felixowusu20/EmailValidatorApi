from fastapi import FastAPI ,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from validator import validate_email_basic
from models import EmailValidationResponse

version = "1"
app = FastAPI(
    title="Email Validator APi",
    description="Validate emails for format,MX and disposable check",
    version=version
)



@app.get("/")
async def read_root():
    return {"WlecomeMessage": "Hello welcome to Email Validator API"}

@app.get("/email/{email}")
async def validate_email(email:str):
    try:
        return validate_email_basic(email)
    except Exception as e:
        raise HTTPException(status_code=500 ,detail=str(e))



    

