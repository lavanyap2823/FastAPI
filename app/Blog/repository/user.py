from sqlalchemy.orm import Session
from Blog import utils, models
from fastapi import Depends, status, HTTPException

def create_user(request, db: Session):
    encrypt_pwd=utils.hashing_passwod(request.password)
    add_user=models.User(name=request.name, email=request.email, password=encrypt_pwd)
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user

def get_user(id: int, db: Session):
    user_result=db.query(models.User).filter(models.User.id==id).first()
    if not user_result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User id {id} not found')
    return user_result