import json

from flask import Flask

from com.codecool.oop import Product
from com.codecool.oop import Other
from sqlalchemy.orm import sessionmaker

from database import engine

app = Flask(__name__)

Session = sessionmaker(bind=engine)


def add_product(product):
    session = Session()
    try:
        session.add(product)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

def get_all_product():
    session = Session()
    query = session.query(Product.Product).all()

    return query

@app.route("/product")
def list():
    data = get_all_product()
    return build_json(data)

@app.route("/product/<id>")
def list_one(id):
    data = get_one_product(id)
    return build_json(data)

def build_json(data):
    dikt = {}

    # dikt = list(map(lambda r: {r.id: r}, data))
    for adat in data:
        temp = {}
        temp['name'] = adat.name
        temp['price'] = adat.price
        temp['descr'] = adat.description
        temp['user_id'] = adat.user_id
        dikt[adat.id] = temp
    print(dikt)
    return json.dumps(dikt)

def get_one_product(id):
    session = Session()
    list = []
    query = session.query(Product.Product).get(id)
    list.append(query)
    return list


if __name__ == "__main__":
    app.secret_key ='KEcskE'
    app.run(
        port=8080,
        debug=True
    )