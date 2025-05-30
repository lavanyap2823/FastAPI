from fastapi import FastAPI, Depends, status, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from Blog.routers import jwttoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return jwttoken.verify_token(token, credentials_exception)
    