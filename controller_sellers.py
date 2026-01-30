from flask import request

from use_case.use_case_sellers import (
    list_sellers_usecase,
    get_seller_usecase,
    create_seller_usecase,
    update_seller_usecase,
    delete_seller_usecase,
)

def register_sellers_routes(app):

    @app.route("/sellers", methods=["GET"])
    def list_sellers():
        return {"sellers": list_sellers_usecase()}

    @app.route("/sellers/<int:seller_id>", methods=["GET"])
    def get_seller(seller_id):
        seller = get_seller_usecase(seller_id)
        if seller is None:
            return {"error": "Seller not found"}, 404
        return seller

    @app.route("/sellers", methods=["POST"])
    def create_seller():
        seller_data = request.json or {}
        body, status = create_seller_usecase(seller_data)
        return body, status

    @app.route("/sellers/<int:seller_id>", methods=["PUT"])
    def update_seller(seller_id):
        seller_data = request.json or {}
        body, status = update_seller_usecase(seller_id, seller_data)
        return body, status

    @app.route("/sellers/<int:seller_id>", methods=["DELETE"])
    def delete_seller(seller_id):
        body, status = delete_seller_usecase(seller_id)
        return body, status



