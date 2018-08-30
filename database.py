import os
import psycopg2
import urllib

from create_app import application

urllib.parse.uses_netloc.append('postgres')
url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
# connection = psycopg2.connect(url)
#     database=url.path,
#     user=url.username,
#     password=url.password,
#     host=url.hostname,
#     port=url.port
# )

# user_name = os.environ.get('PSQL_USER_NAME')
# password = os.environ.get('PSQL_PASSWORD')
# engine = create_engine("postgresql://{user_name}:{password}@localhost:5432/shitwishproducts".format(
#             user_name=user_name,
#             password=password
#             ))

# application.db.Model.metadata.create_all(connection)

