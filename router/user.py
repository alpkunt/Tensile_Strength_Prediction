from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay, UserUpdate, UserDisplay2
from db.database import get_db
from db import db_user
from typing import List


router = APIRouter(
    prefix= '/user',
    tags = ['user']
)


#create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)


@router.get("/username/{username}", response_model=UserDisplay)
def read_user_by_username(username : str, db:Session = Depends(get_db)):
    return db_user.get_user_by_username(username,db)

# read all user
# dikkat read all dediğimiz için, response bir liste olmalı!
@router.get('/', response_model = List[UserDisplay2])
def read_all_user(db: Session = Depends(get_db)):
    return db_user.get_all_user(db)


#read user by email, dikkat burda mail adresleri aynı olan userlar getirilir? ya da database de mail adresi unique yapılır!
@router.get("/email/{email}", response_model=UserDisplay)
def read_user_by_email(email : str, db:Session = Depends(get_db)):
    return db_user.get_user_by_email(email, db)



# read user
@router.get("/id/{id}", response_model=UserDisplay)
def read_user(id: int, db:Session = Depends(get_db)):
    return db_user.get_user(id, db)

#read user more filter?
@router.get("/{id}/{email}", response_model=UserDisplay)
def read_user_id_email(id: int, email : str, db:Session = Depends(get_db)):
    return db_user.get_user_email_id(id, email, db)


@router.put('{id}/update2/')
def update_user(id: int, request: UserUpdate, db: Session = Depends(get_db)) -> object:
    return db_user.update_user_optional_fields(id, request, db)

# delete user

@router.delete("/delete/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user_by_id(id, db)