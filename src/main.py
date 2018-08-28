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


def build_json(data):
    dikt = {}
    page = {}
    counter = 0
    page = 1

    # dikt = list(map(lambda r: {r.id: r}, data))
    for adat in data:
        temp = {}
        temp['name'] = adat.name
        temp['price'] = adat.price
        temp['descr'] = adat.description
        temp['user_id'] = adat.user_id
        if len(data) >=10:
            temp['on_page'] = page
        dikt[adat.id] = temp
        counter += 1

        if counter % 10 == 0:
            page += 1


    print(dikt)
    return json.dumps(dikt)

def build_json_from_list(data):
    id = 0
    name = 1
    price = 2
    descr = 3
    user_id = 4

    dikt = {}

    for adat in data:
        temp = {}
        temp['name'] = adat[name]
        temp['price'] = adat[price]
        temp['descr'] = adat[descr]
        temp['user_id'] = adat[user_id]

        dikt[str(adat[id])] = temp

    return json.dumps(dikt)


def get_one_product(id):
    session = Session()
    list = []
    query = session.query(Product.Product).get(id)
    list.append(query)
    return list

def get_product_on_page():
    session = Session()
    list = []
    query = session.query(Product.Product).get()

def get_prod_by_user(id):
    session = Session()
    query = session.execute(
                    "SELECT * FROM product"
                    " WHERE product.user_id=:param",
                    {"param": id}
            ).fetchall()

    return query


@app.route("/product")
def list():
    data = get_all_product()
    return build_json(data)

@app.route("/product/<id>")
def list_one(id):
    data = get_one_product(id)
    return build_json(data)

@app.route("/product/user/<id>")
def get_product_by_user(id):
    data = get_prod_by_user(id) #give back a list with tuples

    return build_json_from_list(data)


if __name__ == "__main__":

     app.secret_key ='KEcskE'
     app.run(
         port=50098,
         debug=True
     )