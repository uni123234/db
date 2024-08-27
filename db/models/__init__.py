"""
This module initializes the database engine, session, and declarative base.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .customer import Customer
from .sale import Sale
from .supply import Supply
from .product import Product

# Create engine
engine = create_engine("sqlite:///my_db.sql", echo=True)

# Create session
Session = sessionmaker(bind=engine)

# Define base class for declarative models
DeclarativeBase = declarative_base()
