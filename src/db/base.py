import os
from dotenv import load_dotenv
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker,relationship
load_dotenv()

try:
    DATABASE_URL = f'postgresql://{os.environ["USERNAME_DB"]}:{os.environ["PASSWORD_DB"]}@{os.environ["HOST_DB"]}:{os.environ["PORT_DB"]}/{os.environ["NAME_DB"]}'
    print(DATABASE_URL)
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
    Base = declarative_base()
except Exception as e:
    pass

class DBContext:
    def __init__(self) -> None:
        self.db = SessionLocal()

    def __enter__(self):
        return self.db
    
    def __exit__(self,et,ev,traceback):
        self.db.close()

