from fastapi import APIRouter, status, Depends
from database import get_db
from schemas import LoginModel, SignUpModel, ResponseModel, UserResponseModel
from sqlalchemy.orm import Session
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi.exceptions import HTTPException 
from typing import List
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder


auth_router = APIRouter(
   prefix="/auth", 
   tags=["auth"]
)

@auth_router.get("/", response_model=List[UserResponseModel], status_code=status.HTTP_200_OK)
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@auth_router.post("/signup", response_model=ResponseModel, status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel, db: Session = Depends(get_db)):
    db_email = db.query(User).filter(User.email == user.email).first()
    if db_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with Email already exists")
    
    db_username = db.query(User).filter(User.username == user.username).first()
    if db_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with Username already exists")

    new_user = User(
        email=user.email,
        username=user.username,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "email": new_user.email,
        "username": new_user.username,
        "is_active": new_user.is_active,
        "is_staff": new_user.is_staff
    }


@auth_router.post("/login", status_code=status.HTTP_202_ACCEPTED)
async def login(user: LoginModel, Authorize: AuthJWT = Depends(),db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email or password"
        )
    
    if not check_password_hash(str(db_user.password), user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email or password"
        )
    
    access_token = Authorize.create_access_token(subject=str(db_user.email))
    refresh_token = Authorize.create_refresh_token(subject=str(db_user.email))

    response = {
         "access_token": access_token,
         "refresh_token": refresh_token
    }

    return {
        "response": jsonable_encoder(response),
        "message": "User logged in successfully"
    }