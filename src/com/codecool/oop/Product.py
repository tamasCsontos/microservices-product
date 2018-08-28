from sqlalchemy import *
from database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    user_id = Column(Integer, nullable=False)
    is_incart = Column(Boolean, nullable=False)

    def __init__(self, name, price, user_id, description=None):
        self.name = name
        self.price = price
        self.user_id = user_id
        self.description = description
        self.is_incart = False
