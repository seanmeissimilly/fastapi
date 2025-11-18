from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from app.db.session import engine
from app.routers import users, auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLModel.metadata.create_all(engine)

app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(users.router, prefix="/users", tags=["users"])


@app.get("/")
async def read_root():
    return {"mensaje": "Hola Mundo"}
