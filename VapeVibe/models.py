import reflex as rx
from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, Relationship

class TimeStampModel(rx.Model):
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)

class Category(TimeStampModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, max_length=50)
    description: Optional[str] = Field(default=None, max_length=300)
    products: List["Product"] = Relationship(back_populates="category")

class Product(TimeStampModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    price: float = Field(default=0.0)
    brand: str = Field(max_length=50)
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="products")
    images: List["Image"] = Relationship(back_populates="product")

class Image(TimeStampModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str = Field(max_length=255)
    caption: Optional[str] = Field(default=None, max_length=500)
    path: str = Field(max_length=255)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    product: Optional[Product] = Relationship(back_populates="images")
    
#* USER DATABASE
class User(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(max_length=50, unique=True)
    email: str = Field(max_length=100, unique=True)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)