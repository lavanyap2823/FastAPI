from Blog.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id=Column(Integer, ForeignKey('users.id'))
    created_by = relationship("User", back_populates='blogs')
    
class User(Base):
    __tablename__='users'
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship("Blog", back_populates='created_by')