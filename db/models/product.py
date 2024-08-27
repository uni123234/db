"""
This module defines the Product model, which represents products in inventory.
Each product is associated with multiple supplies and sales.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import DeclarativeBase

class Product(DeclarativeBase):
    """
    Product model that stores information about the products in inventory.
    Each product is linked to its supplies and sales.
    """
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    stock = Column(Integer)

    supplies = relationship("Supply", back_populates="product")
    sales = relationship("Sale", back_populates="product")
