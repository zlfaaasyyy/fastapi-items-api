from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    # Nama tabel di database
    __tablename__ = "items"

    # Kolom-kolom tabel
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)