from jwt import encode, decode
from jwt import exceptions
from os import getenv
from fastapi.responses import JSONResponse

def write_token(data:dict):
    token = encode(payload={**data}, key=getenv('SECRET_KEY'), algorithm="HS256")
    return token
    
def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv('SECRET_KEY'), algorithms=["HS256"])
        decode(token, key=getenv('SECRET_KEY'), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)

    
