from pydantic import BaseModel

# Schema dasar (untuk digunakan sebagai inheritance)
class ItemBase(BaseModel):
    name: str
    description: str | None = None

# Schema untuk pembuatan data (opsional untuk tugas GET, tapi good practice)
class ItemCreate(ItemBase):
    pass

# Schema untuk respons API (Output)
# from_attributes=True memungkinkan Pydantic membaca data dari model SQLAlchemy
class Item(ItemBase):
    id: int
    
    class Config:
        from_attributes = True