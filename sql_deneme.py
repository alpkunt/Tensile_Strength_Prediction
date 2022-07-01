from sqlalchemy.orm import relationship

from db.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, JSON, ForeignKey, DateTime

from datetime import datetime, timezone

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    new_data = relationship("Data_Add", back_populates="user")

class Data_Add(Base):
    __tablename__ = 'added_data'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="new_data")

alper = User()
added_data = Data_Add()

added_data.user = alper
print(alper.new_data)

