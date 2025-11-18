from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserRead
from app.crud.user import get_user, create_user
from app.deps.dependencies import get_db
from sqlmodel import Session, select
from app.models.user import User as UserModel

router = APIRouter()

@router.post("/", response_model=UserRead)
def create(payload: UserCreate, session: Session = Depends(get_db)):
    existing = session.exec(select(UserModel).where(UserModel.username == payload.username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="username exists")
    user = UserModel(username=payload.username, email=payload.email)
    # hash password outside or service; aquí simplificado
    return create_user(session, user)

@router.get("/{user_id}", response_model=UserRead)
def read(user_id: int, session: Session = Depends(get_db)):
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="not found")
    return user