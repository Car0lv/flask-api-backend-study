from flask import request

from use_case.use_case_sales import (
    list_sales_usecase,
    get_sale_usecase,
    create_sale_usecase,
    update_sale_usecase,
    delete_sale_usecase,
)

def register_sales_routes(app):

    @app.route("/sales", methods=["GET"])
    def list_sales():
        return {"sales": list_sales_usecase()}

    @app.route("/sales/<int:sale_id>", methods=["GET"])
    def get_sale(sale_id):
        sale = get_sale_usecase(sale_id)
        if sale is None:
            return {"error": "Sale not found"}, 404
        return sale

    @app.route("/sales", methods=["POST"])
    def create_sale():
        sale_data = request.json or {}
        body, status = create_sale_usecase(sale_data)
        return body, status

    @app.route("/sales/<int:sale_id>", methods=["PUT"])
    def update_sale(sale_id):
        sale_data = request.json or {}
        body, status = update_sale_usecase(sale_id, sale_data)
        return body, status

    @app.route("/sales/<int:sale_id>", methods=["DELETE"])
    def delete_sale(sale_id):
        body, status = delete_sale_usecase(sale_id)
        return body, status



