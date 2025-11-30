# src/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from pathlib import Path

DB_PATH = Path("/opt/pymc_repeater/data/repeater.db")
DB_PATH.parent.mkdir(exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH}", future=True, echo=False)
SessionLocal = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()