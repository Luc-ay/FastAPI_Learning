from sqlalchemy import Column, Integer, String, Boolean, Text
from database import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(String)

    def __repr__(self):
        return f'<User {self.username}'