from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os
load_dotenv()

db_url = os.environ.get('DB_URI')

engine = create_engine(db_url, pool_size=100, echo=False)
session = scoped_session(sessionmaker())

def init_session():
    session.configure(bind = engine)
    from models.base import Base
    Base.metadata.create_all(bind = engine)
    
