import json


from flask import Flask, request, Response
from com.codecool.oop import Product
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
    if len(data) != 0:
        for adat in data:
            temp = {}
            temp['name'] = adat.name
            temp['price'] = adat.price
            temp['descr'] = adat.description
            temp['user_id'] = adat.user_id
            temp['is_incart'] = adat.is_incart
            if len(data) >=10:
                temp['on_page'] = page
            dikt[adat.id] = temp
            counter += 1

            if counter % 10 == 0:
                page += 1


        print(dikt)
        return json.dumps(dikt)
    else:
        return Response(status=418)


def build_json_from_list(data):

    if len(data) != 0:
        id = 0
        name = 1
        price = 2
        descr = 3
        user_id = 4
        is_incart = 5

        dikt = {}

        for adat in data:
            temp = {}
            temp['name'] = adat[name]
            temp['price'] = adat[price]
            temp['descr'] = adat[descr]
            temp['user_id'] = adat[user_id]
            temp['is_incart'] = adat[is_incart]

            dikt[str(adat[id])] = temp

        return json.dumps(dikt)
    else:
        return Response(status=418)


def get_one_product(id):
    session = Session()
    list = []
    query = session.query(Product.Product).get(id)
    if query != None:
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


@app.route("/product", methods=['POST', 'GET'])
def list():
    if request.method == 'GET':
        data = get_all_product()
        return build_json(data)
    elif request.method == 'POST':
        new_product = Product.Product(request.form['name'], request.form['price'], request.form['user_id'], request.form['descr'])
        add_product(new_product)
        return 'OK'


@app.route("/product/<id>", methods=['GET'])
def list_one(id):
    if request.method == 'GET':
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
