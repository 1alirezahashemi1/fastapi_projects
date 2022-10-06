from typing import List
from fastapi import APIRouter , Depends
from db.models import DbUser
from schemas import UserBase, UserDisplay
from db.database import get_db
import orm_user
from sqlalchemy.orm import Session
from orm_user import create_user, update_user

router = APIRouter(
    prefix= '/user',
    tags= ['user']
)

@router.post("/",response_model = UserDisplay)
def user(request: UserBase,db: Session = Depends(get_db)):
    return create_user(db,request)

@router.get("/",response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return orm_user.retrieve_all(db)
    
@router.post("/update/{id}")
def update_user_detail(id: int,request: UserBase,db: Session = Depends(get_db)):
    return orm_user.update_user(db,id,request)

@router.post("/delete/{id}")
def delete(id: int,db: Session = Depends(get_db)):
    return orm_user.user_delete(db,id)

@router.post("/search/{id}")
def user_instance(id: int,db: Session = Depends(get_db)):
    return orm_user.get_user(db,id)
