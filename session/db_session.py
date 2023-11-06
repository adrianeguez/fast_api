from sqlalchemy.orm import sessionmaker, declarative_base
import sqlalchemy
from sqlmodel import create_engine, Session

engine = create_engine(
    "sqlite:///ejemplo.db",
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=True  # Log generated SQL
)


engine2 = sqlalchemy.create_engine(
    "sqlite:///ejemplo.db",
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=True  # Log generated SQL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine2)

Base = declarative_base()


def get_session():
    with Session(engine) as session:
        yield session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()