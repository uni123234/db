"""
This module defines the Customer model, representing customers in the database.
Each customer is associated with multiple sales.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import DeclarativeBase

class Customer(DeclarativeBase):
    """
    Customer model that stores information about customers.
    Each customer is linked to their respective sales.
    """
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    sales = relationship("Sale", back_populates="customer")
