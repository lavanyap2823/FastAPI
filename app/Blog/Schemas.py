from pydantic import BaseModel
from typing import List
from pydantic.config import ConfigDict

class Blog(BaseModel):
    title: str
    body: str
       
class User(BaseModel):
    name: str
    email: str
    password: str
    model_config = ConfigDict(from_attributes=True)
    
class BaseDisplayUser(BaseModel):
    name: str
    email: str
    
    model_config = ConfigDict(from_attributes=True)

class showBlog(BaseModel):
    title: str
    body: str
    created_by: BaseDisplayUser
    
    model_config = ConfigDict(from_attributes=True)
    
class DisplayUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    
    model_config = ConfigDict(from_attributes=True)
    
    
class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

