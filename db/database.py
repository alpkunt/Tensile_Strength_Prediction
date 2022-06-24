import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

db_dict = {
    "sqlite": {
        "env_url": os.getenv("SQLALCHEMY_DATABASE_URL_sqlite"),
        "params": {"check_same_thread": False}
    },
    "postgresql": {
        "env_url": os.getenv("SQLALCHEMY_DATABASE_URL_sqlite"),
        "params": None
    }
}


def chose_database1(db_name: str) -> object:
    SQLALCHEMY_DATABASE_URI = db_dict[db_name]["env_url"]
    params = db_dict[db_name]["params"]
    engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args=params)
    return engine

def chose_database(db_name: str) -> object:
    if db_name == "sqlite":
        SQLALCHEMY_DATABASE_URI_sqlite = os.getenv("SQLALCHEMY_DATABASE_URL_sqlite")

        engine = create_engine(
            SQLALCHEMY_DATABASE_URI_sqlite,
            connect_args={"check_same_thread": False}
        )
        return engine

    if db_name == "postgresql":
        SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        return engine


# chose database for development or production
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=chose_database("sqlite"))

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
