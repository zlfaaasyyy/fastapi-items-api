from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db, SessionLocal  # ✅ SessionLocal ditambahkan

# Membuat tabel database berdasarkan models.py
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Endpoint GET /items/ (Membaca semua data)
@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items

# Endpoint GET /items/{id} (Membaca data berdasarkan ID)
@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# --- Script Tambahan untuk Seed Data ---
@app.on_event("startup")
def seed_data():
    db = SessionLocal()  # Sekarang SessionLocal sudah dikenali ✅
    if db.query(models.Item).count() == 0:
        dummy_items = [
            models.Item(name="Laptop", description="Laptop Gaming"),
            models.Item(name="Mouse", description="Mouse Wireless"),
            models.Item(name="Keyboard", description="Mechanical Keyboard"),
        ]
        db.add_all(dummy_items)
        db.commit()
    db.close()