import os
import psycopg2
import urllib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

urllib.parse.uses_netloc.append('postgres')
url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
connection = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

# user_name = os.environ.get('PSQL_USER_NAME')
# password = os.environ.get('PSQL_PASSWORD')
# engine = create_engine("postgresql://{user_name}:{password}@localhost:5432/shitwishproducts".format(
#             user_name=user_name,
#             password=password
#             ))

Base.metadata.create_all(connection)

