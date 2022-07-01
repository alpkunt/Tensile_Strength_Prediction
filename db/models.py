from sqlalchemy.orm import relationship

from db.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, JSON, ForeignKey, DateTime

from datetime import datetime, timezone


def get_utc_now_timestamp() -> datetime:
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)


# TODO: kaynak : https://stackoverflow.com/questions/7548033/how-to-define-two-relationships-to-the-same-table-in-sqlalchemy --->
#  Bir tabloda 2 relationship yapmalıyım! yukarıda örneği buldum!



class Tensile_Strength_Predictions(Base):
    __tablename__ = "tsp"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=get_utc_now_timestamp())
    composition = Column(JSON)
    prediction_method = Column(String)
    prediction_result = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    client_ip = Column(String(256))
    user = relationship('User', back_populates='predictions')


class New_UTS_Data(Base):
    __tablename__ = "df_uts"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime(timezone=True))
    # I give default value very low, so later we dont wana waste time to impute, we can mask or change anytime we want!
    #elements = ["NT", "QT", "TT", "C", "Si", "Mn", "P", "S", "Ni", "Cr", "Cu", "Mo"]

    NT = Column(Float, default=0.00001)
    QT = Column(Float, default=0.00001)
    TT = Column(Float, default=0.00001)
    carbon = Column(Float, default=0.00001)
    silicon = Column(Float, default=0.00001)
    manganese = Column(Float, default=0.00001)
    phosphorus = Column(Float, default=0.00001)
    sulphur = Column(Float, default=0.00001)
    nickel = Column(Float, default=0.00001)
    chromium = Column(Float, default=0.00001)
    copper = Column(Float, default=0.00001)
    molybdenum = Column(Float, default=0.00001)
    creater_id = Column(Integer, ForeignKey("users.id"))
    approved = Column(Boolean, default=False)
    approved_by_id = Column(Integer, ForeignKey("users.id"))
    user = relationship('User', back_populates='approvals', foreign_keys=[approved_by_id])
    user_list = relationship('User', back_populates='created_uts_data_list', foreign_keys=[creater_id])

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, autoincrement=True, primary_key=True)
    created_date = Column(DateTime, default=get_utc_now_timestamp())
    username = Column(String, unique=True)
    email = Column(String)
    hashed_password = Column(String)
    is_Active = Column(Boolean, default=True)
    predictions = relationship('Tensile_Strength_Predictions',
                               foreign_keys="Tensile_Strength_Predictions.user_id",
                               back_populates='user',
                               cascade="all, delete-orphan")
    approvals = relationship('New_UTS_Data',
                             foreign_keys='New_UTS_Data.approved_by_id',
                             back_populates='user',
                             cascade="all, delete-orphan")
    created_uts_data_list = relationship('New_UTS_Data',
                                foreign_keys="New_UTS_Data.creater_id",
                                back_populates='user_list',
                                cascade="all, delete-orphan")

# kaynak : https://stackoverflow.com/questions/39869793/when-do-i-need-to-use-sqlalchemy-back-populates
