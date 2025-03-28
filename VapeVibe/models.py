import reflex as rx
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional
from sqlmodel import Field, Relationship

class Category(rx.Model, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True, max_length=50)
    description: Optional[str] = Field(max_length=300)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    products: list["Product"] = Relationship(back_populates="category")

class Product(rx.Model, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True, max_length=100)
    description: Optional[str] = Field(max_length=500)
    price: float
    image_url: str = Field(max_length=500)
    brand: str = Field(max_length=50)
    flavor: str = Field(max_length=50)
    device_type: str = Field(max_length=30)
    battery: bool
    capacity: int
    nicotine: Optional[str] = Field(max_length=20)
    category_id: UUID = Field(foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="products")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
class Image(rx.Model, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    filename: str = Field(max_length=255)
    caption: str = Field(max_length=500)
    path: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)