from flask_sqlalchemy import SQLAlchemy
from api import app
import os


basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
db.init_app(app)


class Sku(db.Model):
    __tablename__ = 'Sku'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))

    def __init__(self, id, product_name):
        self.id = id
        self.product_name = product_name


class Storage(db.Model):
    __tablename__ = 'Storage'
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.String)
    sku = db.Column(db.Integer)

    def __init__(self, id, stock, sku):
        self.id = id
        self.stock = stock
        self.sku = sku


class Order(db.Model):
    __tablename__ = 'Order'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(200))

    def __init__(self, id, customer_name):
        self.id = id
        self.customer_name = customer_name


class OrderLine(db.Model):
    __tablename__ = 'OrderLine'
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __init__(self, id, sku, quantity):
        self.id = id
        self.sku = sku
        self.quantity = quantity