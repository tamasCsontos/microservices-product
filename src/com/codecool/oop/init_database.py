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

    def __init__(self, name, price, user_id, description=None):
        self.name = name
        self.price = price
        self.user_id = user_id
        self.description = description


user_name = os.environ.get('PSQL_USER_NAME')
password = os.environ.get('PSQL_PASSWORD')
engine = create_engine("postgresql://{user_name}:{password}@localhost:5432/shitwishproducts".format(
            user_name=user_name,
            password=password
            ))
Base.metadata.create_all(engine)

product = Product.Product('Pulcsi', 10, 1, 'Nagymama kötötte pulcsi.')
add_product(product)
product2 = Product.Product('Szék', 50, 1, 'Ülni lehet rajta.')
add_product(product2)
product3 = Product.Product('Jojo', 5, 1)
add_product(product3)
