from fastapi import FastAPI
from router import user, predictions, new_data
from db import models
from db.database import chose_database
from auth import authentication

models.Base.metadata.create_all(bind=chose_database("sqlite"))

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(predictions.router)
app.include_router(new_data.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
