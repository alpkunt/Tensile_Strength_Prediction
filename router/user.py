from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/get_user/{id}")
async def get_user_by_id(id:int):
    return "ok"

@router.post("/create_user")
async def create_user():
    return "ok"

@router.patch("/patch_user")
async def patch_user():
    return "ok"

@router.delete("/delete_user/{id}")
async def delete_user_by_id():
    return "ok"