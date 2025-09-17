from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
   # id: Optional[int]
   email: str
   username: str
   password: str
   is_active: Optional[bool] = True
   is_staff: Optional[bool] = False


   class Config:
      orm_mode = True
      schema_extra = {
         "example": {
            "username": "john_doe",
            "email": "johndoe@gmail.com",
            "password": "strongpassword123",
            "is_active": True,
            "is_staff": False
         }
      }


class ResponseModel(BaseModel):
   email: str
   username: str
   is_active: Optional[bool] = True
   is_staff: Optional[bool] = False

   class Config:
      from_attributes = True


class UserResponseModel(BaseModel):
   id: Optional[int]
   email: str
   username: str
   is_active: Optional[bool] = True
   is_staff: Optional[bool] = False

   class Config:
      orm_mode = True


class LoginModel(BaseModel):
   email: str
   password: str

   class Config:
      from_attributes = True


class Settings(BaseModel):
   authjwt_secret_key: str = "5bb7593cf255881150715912038cec856e248159c3934f460cf5eb5288348582"


