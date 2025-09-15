from database import engine, Base
from schemas import User

Base.metadata.create_all(bind=engine)