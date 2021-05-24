from app import app
from app.models.product import Product

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route("/extract/<product_id>")
def extract(product_id):
    product = Product(product_id)
    product.extract_product()
    product.save_to_json()
    return str(product)

@app.route("/products")
def products():
    pass

@app.route("/opinions/<product_id>")
def product(product_id):
    pass

@app.route("/charts/<product_id>")
def charts():
    pass