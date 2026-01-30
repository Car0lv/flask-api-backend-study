from database.connection import SessionLocal
from database.models.sellers import Seller


def _seller_to_dict(seller: Seller) -> dict:
    return {
        "id": seller.id,
        "name": seller.name,
    }


def get_sellers_repository():
    session = SessionLocal()
    try:
        sellers = session.query(Seller).all()
        return [_seller_to_dict(s) for s in sellers]
    finally:
        session.close()


def get_seller_by_id_repository(seller_id: int):
    session = SessionLocal()
    try:
        seller = session.query(Seller).filter(Seller.id == seller_id).first()
        if seller is None:
            return None
        return _seller_to_dict(seller)
    finally:
        session.close()


def create_seller_repository(seller_data: dict):
    session = SessionLocal()
    try:
        seller = Seller(name=seller_data["name"])
        session.add(seller)
        session.commit()
        session.refresh(seller)
        return _seller_to_dict(seller)
    finally:
        session.close()


def update_seller_repository(seller_id: int, seller_data: dict):
    session = SessionLocal()
    try:
        seller = session.query(Seller).filter(Seller.id == seller_id).first()
        if seller is None:
            return None

        if "name" in seller_data:
            seller.name = seller_data["name"]

        session.commit()
        session.refresh(seller)
        return _seller_to_dict(seller)
    finally:
        session.close()


def delete_seller_repository(seller_id: int) -> bool:
    session = SessionLocal()
    try:
        seller = session.query(Seller).filter(Seller.id == seller_id).first()
        if seller is None:
            return False

        session.delete(seller)
        session.commit()
        return True
    finally:
        session.close()


