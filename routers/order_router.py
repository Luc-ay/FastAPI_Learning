from fastapi import APIRouter


order_router = APIRouter(
   prefix="/order", 
   tags=["order"]
)

@order_router.get("/")
def read_root():
    return {"message": "Welcome to the auth router"}