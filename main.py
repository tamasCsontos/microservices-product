import json

from create_app import application
from flask import request, Response, redirect

import Product


app = application.app
session = application.db.session


def add_product(product):
    try:
        session.add(product)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def delete_product(product):
    try:
        session.delete(product)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def get_all_product():
    query = session.query(Product.Product).all()

    return query


def build_json(data):
    dikt = {}
    counter = 0
    page = 1

    # dikt = list(map(lambda r: {r.id: r}, data))
    if len(data) != 0:
        for adat in data:
            temp = {}
            temp['name'] = adat.name
            temp['price'] = adat.price
            temp['descr'] = adat.description
            temp['img'] = adat.img
            temp['user_id'] = adat.user_id
            temp['is_incart'] = adat.is_incart
            temp['is_active'] = adat.is_active
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
        img = 6
        is_active = 7

        dikt = {}

        for adat in data:
            temp = {}
            temp['name'] = adat[name]
            temp['price'] = adat[price]
            temp['descr'] = adat[descr]
            temp['img'] = adat[img]
            temp['user_id'] = adat[user_id]
            temp['is_incart'] = adat[is_incart]
            temp['is_active'] = adat[is_active]

            dikt[str(adat[id])] = temp

        return json.dumps(dikt)
    else:
        return Response(status=418)


def get_one_product(id):
    list = []
    query = session.query(Product.Product).get(id)
    if query != None:
        list.append(query)
        session.close()
    return list


def get_product_on_page():
    list = []
    query = session.query(Product.Product).get()


def get_prod_by_user(id):
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
        if "img" in request.get_json() and "descr" in request.get_json():
            new_product = Product.Product(request.json['name'], request.json['price'], request.json['user_id'],
                                          request.json['img'], request.json['descr'])
        elif "descr" in request.json:
            new_product = Product.Product(request.json['name'], request.json['price'], request.json['user_id'],
                                          "https://i.imgur.com/jNikxeh.png",
                                          request.json['descr'])
        elif "img" in request.json:
            new_product = Product.Product(request.json['name'], request.json['price'], request.json['user_id'],
                                          request.json['img'])
        else:
            new_product = Product.Product(request.json['name'], request.json['price'], request.json['user_id'])
        add_product(new_product)
        return redirect("/")


@app.route("/product/<id>", methods=['DELETE'])
def remove_product(id):
    try:
        product = get_one_product(id)
        delete_product(product[0])
        return 'OK'
    except IndexError:
        return Response(status=418)


@app.route("/product/<id>", methods=['PUT'])
def modify_product(id):
    new_data = request.form.to_dict()
    if "is_incart" in new_data:
        new_data['is_incart'] = bool(new_data['is_incart'])
    if "is_active" in new_data:
        new_data['is_active'] = bool(new_data['is_active'])
    try:
        modified = session.query(Product.Product)\
            .filter(Product.Product.id == id)\
            .update(new_data)
        if modified == 0:
            return Response(status=418)
        elif modified == 1:
            session.commit()
            return 'OK'
    except Exception as e:
        print(e)
        session.rollback()


@app.route("/product/<id>", methods=['GET'])
def list_one(id):
    if request.method == 'GET':
        data = get_one_product(id)
        return build_json(data)


@app.route("/product/user/<id>")
def get_product_by_user(id):
    data = get_prod_by_user(id) #give back a list with tuples

    return build_json_from_list(data)


app.secret_key ='KEcskE'

print('BBBBBBBB')
if __name__ == "__main__":
    print('AAAAAAAA')
    app.run(
         port=50098,
         debug=True
     )
