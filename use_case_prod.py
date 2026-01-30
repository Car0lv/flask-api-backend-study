from Repository.repository_prod import (
    get_products_repository,
    get_product_by_id_repository,
    create_product_repository,
    update_product_repository,
    delete_product_repository,
)

def list_products_usecase():
    return get_products_repository()

def get_product_usecase(product_id: int):
    return get_product_by_id_repository(product_id)

def create_product_usecase(product_data: dict):
    if not product_data or "name" not in product_data:
        return {"error": "Field 'name' is required"}, 400
    return create_product_repository(product_data), 201

def update_product_usecase(product_id: int, product_data: dict):
    updated = update_product_repository(product_id, product_data or {})
    if updated is None:
        return {"error": "Product not found"}, 404
    return updated, 200

def delete_product_usecase(product_id: int):
    ok = delete_product_repository(product_id)
    if not ok:
        return {"error": "Product not found"}, 404
    return "", 204
