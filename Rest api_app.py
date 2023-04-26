from flask import Flask,request
from api_model import db,Product,Customer

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:123456@satyanshu/api"
db.init_app(app)
# db= SQLALchemy(app)   if classes were present in this app itself...
@app.route("/")
def index():
    return"<h1>Hello</h1>"

# @app.route("/create",methods=["POST"]) 
# def create():
#     db.create_all()  
#     return ("all tables created")

@app.route("/products/<id>",methods=["POST"])
def add_product(id):
    product=Product(product_id=request.json["prod_id"],name=request.json["name"],price=request.json["price"],country=request.json["country"],description=request.json["description"])
    db.session.add(product)
    db.session.commit()
    return {"name":product.name,"price":product.price,"country":product.country,"description":product.description}

@app.route("/products")
def get_products(): 
    products= Product.query.all()
    output=[]
    for i in products:
        output_data={"name":i.name,"price":i.price,"country":i.country,"description":i.description}
        output.append(output_data)
    return {"products":output}

@app.route("/products/<id>")
def get_product(id):
    product=Product.query.get(id)
    if product is None:
        return{"error":"not found"}
    else:
        return  {"name": product.name,"price": product.price,"country": product.price,"description":product.description,}

@app.route("/products/<id>",methods=["DELETE"])
def delete_product(id):
    product=Product.query.get(id)
    if product is None:
        return {"error":"not found"}
    db.session.delete(product)
    db.session.commit()
    return{"message":"product deleted"}

@app.route("/customers/<id>",methods=["POST"])
def add_customer(id):
    cust=Customer(name=request.json["name"],email=request.json["email"])
    db.session.add(cust)
    db.session.commit()
    return {"name":cust.name,"email":cust.email}

@app.route("/customers/<id>")
def get_customer(id):
    cust=Customer.query.get(id)
    if cust is None:
        return{"error":"not found"}
    else:
         return  {"customer_id":cust.customer_id,"name": cust.name,"email":cust.email}

@app.route("/customers")
def get_customers():
    cust = Customer.query.all()
    output=[]
    for i in cust:
        d={"customer_id":i.customer_id,"name":i.name,"email":i.email}
        output.append(d)
    return output

if __name__=="__main__":
    app.run(debug=True)
  