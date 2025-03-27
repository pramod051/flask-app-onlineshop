from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Sample products
products = [
    {"id": 1, "name": "Laptop", "price": 800},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Headphones", "price": 100}
]

# Home Page - List Products
@app.route('/')
def index():
    return render_template('index.html', products=products)

# Add to Cart
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    session['cart'].append(product_id)
    session.modified = True
    return redirect(url_for('cart'))

# View Cart
@app.route('/cart')
def cart():
    cart_items = [p for p in products if p["id"] in session.get('cart', [])]
    return render_template('cart.html', cart=cart_items)

# Clear Cart
@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
