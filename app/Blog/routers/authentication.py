from fastapi import APIRouter
from Blog import Schemas, database
from sqlalchemy.orm import Session
from Blog import utils, models
from Blog.utils import Hash
from fastapi import Depends, status, HTTPException
from Blog.routers import jwttoken
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")
    
    access_token_expires = timedelta(minutes=jwttoken.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwttoken.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token":access_token, "token_type":"bearer"}