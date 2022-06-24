from fastapi import FastAPI
from router import user



app = FastAPI()

app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

