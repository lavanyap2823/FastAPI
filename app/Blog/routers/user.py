from fastapi import APIRouter
from Blog import Schemas, database
from sqlalchemy.orm import Session
from fastapi import Depends
from Blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', response_model=Schemas.DisplayUser)
def create_user(request: Schemas.User, db: Session=(Depends(database.get_db))):
    return user.create_user(request, db)

@router.get('/{id}', response_model=Schemas.DisplayUser)
def get_user(id: int, db: Session=(Depends(database.get_db))):
    return user.get_user(id, db)