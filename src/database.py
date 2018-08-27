from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://localhost:5432/shitwishproducts")

Base = declarative_base()

Base.metadata.create_all(engine)

