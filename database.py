from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Fas.kid1@localhost/fastapi-blog'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)