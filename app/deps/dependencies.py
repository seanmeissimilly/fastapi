from fastapi import Depends
from app.db.session import get_session
from sqlmodel import Session

def get_db(session: Session = Depends(get_session)):
    yield session