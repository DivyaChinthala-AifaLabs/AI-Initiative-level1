from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/auth')

@router.post('/login')
def login():
    return {"message": "Login successful"}

@router.post('/register')
def register():
    return {"message": "User registerd successfully"}

class User(BaseModel):
    email: str

@router.post('/update-password')
def updatePassword(data: User):
    return {"message": f"Password updated successfully for user {data.email}"}
    