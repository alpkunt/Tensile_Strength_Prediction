from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import CompositionRequest, CompRequest_New_data
from db.database import get_db
from db import db_new_data
from typing import List
from enum import Enum

router = APIRouter(
    prefix='/new_data',
    tags=['add data']
)


@router.post("/")
async def add_new_data(request: CompRequest_New_data, db: Session = Depends(get_db)):
    return db_new_data.insert_new_uts_data(request, db)
