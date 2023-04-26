from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Product(db.Model):
    product_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    price= db.Column(db.Float,unique=True,nullable=False)
    country=db.Column(db.String(120),unique=True,nullable=False)
    description = db.Column(db.String(120))

class Customer(db.Model):
    customer_id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    email=db.Column(db.String(80),unique=True,nullable=False)

   