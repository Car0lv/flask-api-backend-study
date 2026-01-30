from Repository.repository_sales import (
    get_sales_repository,
    get_sale_by_id_repository,
    create_sale_repository,
    update_sale_repository,
    delete_sale_repository,
)

def list_sales_usecase():
    return get_sales_repository()

def get_sale_usecase(sale_id: int):
    return get_sale_by_id_repository(sale_id)

def create_sale_usecase(sale_data: dict):
    if not sale_data:
        return {"error": "Request body is required"}, 400

    required_fields = ["product_id", "seller_id", "quantity"]
    missing = [f for f in required_fields if f not in sale_data]
    if missing:
        return {"error": f"Missing fields: {', '.join(missing)}"}, 400

    created = create_sale_repository(
        product_id=sale_data["product_id"],
        seller_id=sale_data["seller_id"],
        quantity=sale_data["quantity"],
    )
    return created, 201

def update_sale_usecase(sale_id: int, sale_data: dict):
    updated = update_sale_repository(sale_id, sale_data or {})
    if updated is None:
        return {"error": "Sale not found"}, 404
    return updated, 200

def delete_sale_usecase(sale_id: int):
    ok = delete_sale_repository(sale_id)
    if not ok:
        return {"error": "Sale not found"}, 404
    return "", 204
