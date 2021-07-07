from flask import Flask,jsonify


app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({'messege': 'pong!'})

from product import products 

@app.route('/product')#  methods=['GET'] por "defecto"
def get_products():
    return jsonify({"productos":products,
                    "messege":"Product's list"
                    })

@app.route('/product/<string:product_name>')
def get_product(product_name):
    #list of matches 
    products_found = [product for product in products 
                      if product['name'] == product_name.lower()]
    if (len(products_found) > 0):
        return jsonify({'product': products_found[0]})
    return jsonify({'message': 'Product Not found'})

if __name__ == '__main__':
    app.run(debug=True, port= 5000) 
    