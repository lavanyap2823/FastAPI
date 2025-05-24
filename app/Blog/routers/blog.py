from fastapi import APIRouter
from typing import List
from Blog import Schemas, database
from sqlalchemy.orm import Session
from fastapi import Depends, status, Response
from Blog.repository import blog
from Blog.routers import oauth2

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.get('/', response_model=List[Schemas.Blog])
def blog_list(db: Session=(Depends(database.get_db)), current_user: Schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Schemas.Blog, db: Session=(Depends(database.get_db)), current_user: Schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session=(Depends(database.get_db)), current_user: Schemas.User=Depends(oauth2.get_current_user)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: Schemas.Blog, db: Session=(Depends(database.get_db)), current_user: Schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Schemas.showBlog)
def show(id: int, response: Response, db: Session=(Depends(database.get_db)), current_user: Schemas.User=Depends(oauth2.get_current_user)):
    return blog.get(id, db)