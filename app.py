from flask import Flask

from controllers.controller_sales import register_sales_routes
from controllers.controller_sellers import register_sellers_routes
from controllers.controller_prod import register_product_routes

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando!"

register_sales_routes(app)
register_sellers_routes(app)
register_product_routes(app)

if __name__ == "__main__":
    app.run(debug=True)



