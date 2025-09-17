# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Fas.kid1@localhost:8080/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency function
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
