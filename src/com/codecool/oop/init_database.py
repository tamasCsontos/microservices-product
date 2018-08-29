import os

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from com.codecool.oop import Product
from main import add_product

Base = declarative_base()


class Prod(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    user_id = Column(Integer, nullable=False)
    is_incart = Column(Boolean, nullable=False)
    img = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False)

    def __init__(self, name, price, user_id, img="https://imgur.com/a/C94poxI", description=None):
        self.name = name
        self.price = price
        self.user_id = user_id
        self.img = img
        self.description = description
        self.is_incart = False
        self.is_active = True


user_name = os.environ.get('PSQL_USER_NAME')
password = os.environ.get('PSQL_PASSWORD')
engine = create_engine("postgresql://{user_name}:{password}@localhost:5432/shitwishproducts".format(
            user_name=user_name,
            password=password
            ))
Base.metadata.create_all(engine)

product = Product.Product('Pullover', 10, 1, "https://imgur.com/a/5gU8F3Q", "It's a clothing.")
add_product(product)
product2 = Product.Product('Chair', 50, 1, "https://imgur.com/a/ehFULsF", 'You can sit on it')
add_product(product2)
product3 = Product.Product('Jojo', 5, 2)
add_product(product3)
