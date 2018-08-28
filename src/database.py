import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

user_name = os.environ.get('PSQL_USER_NAME')
password = os.environ.get('PSQL_PASSWORD')
engine = create_engine("postgresql://{user_name}:{password}@localhost:5432/shitwishproducts".format(
            user_name=user_name,
            password=password
            ))

Base.metadata.create_all(engine)

