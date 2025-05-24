from fastapi import FastAPI
from Blog import models
from Blog.database import engine
from sqlalchemy.orm import Session
from Blog.routers import blog, user, authentication

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)






        
    
    