from sqlmodel import Session, select
from app.models.user import User

def get_user(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)

def get_user_by_username(session: Session, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    return session.exec(statement).first()

def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user