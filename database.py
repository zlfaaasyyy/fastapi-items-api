from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Menggunakan SQLite sesuai permintaan tugas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Membuat engine koneksi
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Pabrik untuk membuat sesi database baru
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Kelas dasar untuk mendefinisikan model ORM
Base = declarative_base()

# Dependency Injection untuk mengelola siklus hidup koneksi database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()