from Blog import models
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status, Response, HTTPException

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request, db: Session):
    new_blog= models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session):
    delete_blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not delete_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    delete_blog.delete(synchronize_session=False)
    db.commit()
    return 'Blog deleted successfully'

def update(id: int, request, db: Session):
    updated_blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not updated_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found!')
    updated_blog.update(request.model_dump(), synchronize_session=False)
    db.commit()
    return "Blog updated"

def get(id: int, db: Session):
    result_id = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not result_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id {id} not found')
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'details': f'Blog id {id} not found'}
    return result_id