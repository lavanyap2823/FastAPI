from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL='sqlite:///./blog.db'


engine=create_engine(SQLALCHEMY_DB_URL, connect_args={'check_same_thread':False})

local_session=sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base=declarative_base()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()

