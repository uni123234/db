"""
This module defines the Supply model which represents the supplies of products.
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import DeclarativeBase

class Supply(DeclarativeBase):
    """
    Supply model that stores information about product supplies.
    Each supply is associated with a product.
    """
    __tablename__ = "supplies"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="supplies")
