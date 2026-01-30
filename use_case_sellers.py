from Repository.repository_sellers import (
    get_sellers_repository,
    get_seller_by_id_repository,
    create_seller_repository,
    update_seller_repository,
    delete_seller_repository,
)

def list_sellers_usecase():
    return get_sellers_repository()

def get_seller_usecase(seller_id: int):
    return get_seller_by_id_repository(seller_id)

def create_seller_usecase(seller_data: dict):
    if not seller_data or "name" not in seller_data:
        return {"error": "Field 'name' is required"}, 400

    created = create_seller_repository(seller_data)
    return created, 201

def update_seller_usecase(seller_id: int, seller_data: dict):
    updated = update_seller_repository(seller_id, seller_data or {})
    if updated is None:
        return {"error": "Seller not found"}, 404
    return updated, 200

def delete_seller_usecase(seller_id: int):
    ok = delete_seller_repository(seller_id)
    if not ok:
        return {"error": "Seller not found"}, 404
    return "", 204
