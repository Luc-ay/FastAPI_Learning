from fastapi import APIRouter


auth_router = APIRouter(
   prefix="/auth", 
   tags=["auth"]
)

@auth_router.get("/")
def read_root():
    return {"message": "Welcome to the auth router"}