from pydantic import BaseModel, Field
from typing import Optional
from typing import List, Dict
from datetime import datetime, timezone
import re
from sqlalchemy.dialects.sqlite import DATETIME

def get_utc_now_timestamp() -> datetime:
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)


# NOT, display olan herşeyde orm mode True diyeceğiz, çunku, display donerken veri tabanı ile data transformu yaparken problem cıkarmıyor!

class Predictions(BaseModel):
    id: int
    #date: datetime
    #prediction_result: float

    class Config:
        orm_mode = True


class Approvals(BaseModel):
    #date: datetime
    id: int

    class Config:
        orm_mode = True


class CreatedDatas(BaseModel):
    date: datetime
    created_uts_data_list: Dict

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    # created_date: Union[datetime, None] = Body(default=None)
    created_date: datetime = Field(get_utc_now_timestamp())
    is_Active: Optional[bool] = True


class UserDisplay(BaseModel):
    created_date: datetime
    username: str
    email: str
    is_Active: Optional[bool] = True
    predictions: List[Predictions]  # yukarda predictions classs olusturduk, aslında liste içinde nested yukardaki predictions listelenecek!
    approvals: List[Approvals]
    #created_uts_data_list: List[CreatedDatas]

    # dikkat get all users dendiğinde, itemsta olduğu gibi geliyor!
    # yani kullanıcının ne kadar ürettiği icerik var hepsi geliyor. Bir mantık hatası var burda
    class Config:
        orm_mode = True


class UserDisplay2(BaseModel):
    username: str
    email: str
    items: List[Predictions] = []

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    # password: Optional[str]


class UserID(UserBase):
    id: int


class CompositionRequest(BaseModel):
    NT: float
    QT: float
    TT: float
    carbon: float
    silicon: float
    manganese: float
    phosphorus: float
    sulphur: float
    nickel: float
    chromium: float
    copper: float
    molybdenum: float

    class Config:
        schema_extra = {
            "example": {
                "NT": 863,
                "QT": 660,
                "TT": 780,
                "carbon": 0.5,
                "silicon": 0.19,
                "manganese": 0.8,
                "phosphorus": 0.011,
                "sulphur": 0.013,
                "nickel": 0.03,
                "chromium": 0.03,
                "copper": 0.01,
                "molybdenum": 0.001
            }
        }

class CompRequest_New_data(CompositionRequest):
    created_date: datetime = Field(get_utc_now_timestamp())
