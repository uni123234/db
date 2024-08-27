"""
This module initializes the database by creating tables and adding initial data.
It defines products, customers, supplies, and sales, and commits them to the database.
"""

from models import DeclarativeBase, engine, Session, Product, Supply, Sale, Customer

# Create the tables in the database
DeclarativeBase.metadata.create_all(engine)

# Start a session
with Session() as session:
    # Create products
    product1 = Product(name="Product1", stock=100)
    product2 = Product(name="Product2", stock=150)

    # Create a customer
    customer1 = Customer(name="Customer1")

    # Create supplies
    supply1 = Supply(quantity=50, product=product1)
    supply2 = Supply(quantity=75, product=product2)

    # Create sales
    sale1 = Sale(quantity=20, product=product1, customer=customer1)
    sale2 = Sale(quantity=30, product=product2, customer=customer1)

    # Add all objects to the session
    session.add_all([product1, product2, customer1, supply1, supply2, sale1, sale2])

    # Commit the session to the database
    session.commit()
