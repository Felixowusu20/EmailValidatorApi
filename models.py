from pydantic import BaseModel

class EmailValidationResponse(BaseModel):
    email:str
    is_valid_formate:bool
    has_mx_record:bool
    is_disposable:bool