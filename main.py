from fastapi import FastAPI
from routers import authRoutes

app = FastAPI()

@app.get("/")
def myFirstFunc():
    return {"message": "Hello FastAPI"}

app.include_router(authRoutes.router)