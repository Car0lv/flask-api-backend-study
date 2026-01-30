from database.connection import SessionLocal
from database.models.product import Product


def _product_to_dict(product: Product) -> dict:
    return {
        "id": product.id,
        "name": product.name,
    }

def get_products_repository():
    session = SessionLocal()
    try:
        products = session.query(Product).all()
        return [_product_to_dict(p) for p in products]
    finally:
        session.close()

def get_product_by_id_repository(product_id: int):
    session = SessionLocal()
    try:
        product = (
            session.query(Product)
            .filter(Product.id == product_id)
            .first()
        )
        if product is None:
            return None
        return _product_to_dict(product)
    finally:
        session.close()

def create_product_repository(product_data: dict):
    session = SessionLocal()
    try:
        new_product = Product(
            name=product_data["name"]
        )
        session.add(new_product)
        session.commit()
        session.refresh(new_product) 
        return _product_to_dict(new_product)
    finally:
        session.close()

def update_product_repository(product_id: int, product_data: dict):
    session = SessionLocal()
    try:
        product = (
            session.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if product is None:
            return None

        if "name" in product_data:
            product.name = product_data["name"]

        session.commit()
        session.refresh(product)
        return _product_to_dict(product)
    finally:
        session.close()

def delete_product_repository(product_id: int) -> bool:
    session = SessionLocal()
    try:
        product = (
            session.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if product is None:
            return False

        session.delete(product)
        session.commit()
        return True
    finally:
        session.close()
