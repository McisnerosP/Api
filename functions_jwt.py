from jwt import encode, decode
from jwt import exceptions
from os import getenv
from fastapi.responses import JSONResponse

SECRET_KEY='eb4ce7120581a602a0222147254c2c7930525a41b0d6ae2d75ec79265e684163'


def write_token(data:dict):
    token = encode(payload={**data}, key="SECRET_KEY", algorithm="HS256")
    return token



def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key="SECRET_KEY", algorithms=["HS256"])
        decode(token, key="SECRET_KEY", algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)

    
