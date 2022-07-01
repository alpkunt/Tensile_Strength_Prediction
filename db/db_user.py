from sqlalchemy.orm import Session
from schemas import UserBase, UserUpdate
from db.models import User
from db.hash import Hash
from fastapi import HTTPException, status



def create_user(request: UserBase, db: Session):
    new_user = User(
        username=request.username,
        email=request.email,
        created_date=request.created_date,
        hashed_password=Hash.bcrypt(request.password),  # buraya tekrar bak!
        is_Active= True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # returning ---> id
    return new_user


def get_all_user(db: Session):
    return db.query(User).limit(5).all()


def get_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User id:{id} is not here!')

    return user


def get_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User :{username} is not here!')

    return user



def get_user_by_email(email: str, db:Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Email :{email} is not here!')

    return user

# dikkat daha fazla filter istiyorsan

def get_user_email_id(id: int, email: str, db: Session):
    return db.query(User).filter(User.id == id).filter(User.email == email).first()


# all required fields update!
def update_user_all_fields(id: int, db: Session, request: UserBase) -> object:
    user = db.query(User).filter(User.id == id)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User id:{id} is not here!')

    user.update(
        {
            User.username: request.username,
            User.email: request.email,
            User.password: Hash.bcrypt(request.password)
        }
    )
    db.commit()
    return 'ok'


def update_user_optional_fields(id: int, request: UserUpdate, db: Session) -> object:
    user = db.query(User).filter(User.id == id)
    if not user.first():  # buraya first() koymayınca user içinde veri geliyor zannederim!
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User id:{id} is not here!')
    user.update(request.dict(exclude_unset=True))
    db.commit()
    # dikkat, return ya da response body olarak direk request body de değiştirdiğimizi değeri gonderiyoruz! request.dict()
    return request.dict(exclude_unset=True)  # exclude unset true diyerek, request body içersinde set edilmemiş değerlerin, response bodye null donmesini önlüyoruz!


def delete_user_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User id:{id} is not here!')
    db.delete(user)
    db.commit()

