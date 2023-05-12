from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from src.db.base import SessionLocal,DBContext
from src.schemas.response_schema import ResponseModel
from src.schemas.Users import users_chema as schemas
from src.models import models 
from src.services import user_services as UserService
from typing import List

router = APIRouter(
    prefix="/api",
    tags=["api"],
    dependencies=[]
)

def get_db():
    with DBContext() as db:
         yield db

@router.post("/init_db", response_model=ResponseModel)
async def create_user(db:Session = Depends(get_db)):
    db_user = await UserService.init_course(db=db)
    return ResponseModel(status_code=200,
                         message="create users",
                         data=db_user
                         )


@router.post("/essay", response_model=ResponseModel)
async def create_user(essay: schemas.Essay,db:Session = Depends(get_db)):
    respone = await UserService.essay(essay=essay,db=db)
    return ResponseModel(status_code=200,
                         message="suggestion",
                         data=respone
                         )

