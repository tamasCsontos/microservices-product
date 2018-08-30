from create_app import application

db = application.db


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, nullable=False)
    is_incart = db.Column(db.Boolean, nullable=False)
    img = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, price, user_id, img="https://imgur.com/a/C94poxI", description=None):
        self.name = name
        self.price = price
        self.user_id = user_id
        self.img = img
        self.description = description
        self.is_incart = False
        self.is_active = True
