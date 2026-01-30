from flask import request

from use_case.use_case_prod import (
    list_products_usecase,
    get_product_usecase,
    create_product_usecase,
    update_product_usecase,
    delete_product_usecase,
)

def register_product_routes(app):

    @app.route("/products", methods=["GET"])
    def list_products():
        return {"products": list_products_usecase()}

    @app.route("/products/<int:product_id>", methods=["GET"])
    def get_product(product_id):
        product = get_product_usecase(product_id)
        if product is None:
            return {"error": "Product not found"}, 404
        return product

    @app.route("/products", methods=["POST"])
    def create_product():
        product_data = request.json or {}
        body, status = create_product_usecase(product_data)
        return body, status

    @app.route("/products/<int:product_id>", methods=["PUT"])
    def update_product(product_id):
        product_data = request.json or {}
        body, status = update_product_usecase(product_id, product_data)
        return body, status

    @app.route("/products/<int:product_id>", methods=["DELETE"])
    def delete_product(product_id):
        body, status = delete_product_usecase(product_id)
        return body, status

