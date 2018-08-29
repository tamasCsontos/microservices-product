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
