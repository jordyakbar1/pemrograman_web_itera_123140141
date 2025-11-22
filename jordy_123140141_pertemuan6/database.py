from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///matakuliah.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_session():
    return SessionLocal()


# Membuat tabel di database jika belum ada
def init_db():
    Base.metadata.create_all(bind=engine)


# Load DB saat modul di-import
init_db()
