from database.connection import SessionLocal
from database.models.sales import Sale
from sqlalchemy.orm import joinedload


def _sale_to_dict(sale: Sale) -> dict:
    return {
        "id": sale.id,
        "quantity": sale.quantity,
        "product": {
            "id": sale.product.id,
            "name": sale.product.name,
        } if sale.product else None,
        "seller": {
            "id": sale.seller.id,
            "name": sale.seller.name,
        } if sale.seller else None,
    }


def get_sales_repository():
    session = SessionLocal()
    try:
        sales = (
            session.query(Sale)
            .options(
                joinedload(Sale.product),
                joinedload(Sale.seller),
            )
            .all()
        )
        return [_sale_to_dict(s) for s in sales]
    finally:
        session.close()


def get_sale_by_id_repository(sale_id: int):
    session = SessionLocal()
    try:
        sale = (
            session.query(Sale)
            .options(
                joinedload(Sale.product),
                joinedload(Sale.seller),
            )
            .filter(Sale.id == sale_id)
            .first()
        )
        if sale is None:
            return None
        return _sale_to_dict(sale)
    finally:
        session.close()


def create_sale_repository(product_id: int, seller_id: int, quantity: int):
    session = SessionLocal()
    try:
        sale = Sale(
            product_id=product_id,
            seller_id=seller_id,
            quantity=quantity,
        )
        session.add(sale)
        session.commit()
        session.refresh(sale)
        return _sale_to_dict(sale)
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def update_sale_repository(sale_id: int, sale_data: dict):
    session = SessionLocal()
    try:
        sale = session.query(Sale).filter(Sale.id == sale_id).first()
        if sale is None:
            return None

        if "product_id" in sale_data:
            sale.product_id = sale_data["product_id"]
        if "seller_id" in sale_data:
            sale.seller_id = sale_data["seller_id"]
        if "quantity" in sale_data:
            sale.quantity = sale_data["quantity"]

        session.commit()
        session.refresh(sale)
        return _sale_to_dict(sale)
    finally:
        session.close()


def delete_sale_repository(sale_id: int) -> bool:
    session = SessionLocal()
    try:
        sale = session.query(Sale).filter(Sale.id == sale_id).first()
        if sale is None:
            return False

        session.delete(sale)
        session.commit()
        return True
    finally:
        session.close()

    

   
