from sqlmodel import create_engine, Session
from app.core.config import DATABASE_URL, ECHO_SQL


engine = create_engine(DATABASE_URL, echo=ECHO_SQL, connect_args={"options": "-c timezone=utc"})

def get_session():
    with Session(engine) as session:
        yield session