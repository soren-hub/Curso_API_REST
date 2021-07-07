from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/prueba')
def prueba():
    return jsonify({'messege': 'todo funcionando!'})

from product import products 

@app.route('/products')#  methods=['GET'] por "defecto"
def get_products():
    return jsonify({"productos":products,
                    "messege":"Product's list"
                    })

@app.route('/products/<string:product_name>')
def get_product(product_name):
    #list of matches 
    products_found = [product for product in products 
                      if product['name'] == product_name.lower()]
    if (len(products_found) > 0):
        return jsonify({'product': products_found[0]})
    return jsonify({'message': 'Product Not found'})

# Create Data Routes
@app.route('/products', methods=['POST'])
def add_product():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    products.append(new_product)
    return jsonify({'products': products})

# Update Data Route
@app.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name):
    products_found = [product for product in products 
                     if product['name'] == product_name]
    if (len(products_found) > 0):
        products_found[0]['name'] = request.json['name']
        products_found[0]['price'] = request.json['price']
        products_found[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': products_found[0]
        })
    return jsonify({'message': 'Product Not found'})

# DELETE Data Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    delete_product = [product for product in products 
                      if product['name'] == product_name]
    if len(delete_product) > 0:
        products.remove(delete_product[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })

if __name__ == '__main__':
    #puedo correr varias api's solo tengo que cambiar 
    #el port, esto diferencia cada api  
    app.run(debug=True, port= 4000) 
    