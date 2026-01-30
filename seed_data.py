from database.connection import SessionLocal
from database.models.product import Product
from database.models.sellers import Seller
from database.models.sales import Sale

def seed_products():
    session = SessionLocal()
    try:
        initial_products = [
            "iPhone",
            "Mac",
            "iPad",
            "Raquete",
            "Rede",
        ]

        for name in initial_products:
            exists = session.query(Product).filter_by(name=name).first()
            if not exists:
                session.add(Product(name=name))

        session.commit()
        print("Produtos iniciais inseridos com sucesso!")
    except Exception as e:
        session.rollback()
        print("Erro ao inserir produtos:", e)
    finally:
        session.close()


def seed_sellers():
    session = SessionLocal()
    try:
        initial_sellers = ["Segio", "Carol", "Isamara"]

        for name in initial_sellers:
            exists = session.query(Seller).filter(Seller.name == name).first()
            if not exists:
                session.add(Seller(name=name))

        session.commit()
        print("Sellers inseridos/verificados com sucesso!")
    except Exception as e:
        session.rollback()
        print("Erro ao inserir sellers:", e)
        raise
    finally:
        session.close()


def seed_sales():
    session = SessionLocal()
    try:
        products = session.query(Product).all()
        sellers = session.query(Seller).all()

        if not products or not sellers:
            raise ValueError("Precisa ter products e sellers no banco antes de seed_sales().")

        examples = [
            (products[0].id, sellers[0].id, 1),
            (products[1].id, sellers[0].id, 2),
            (products[2].id, sellers[1].id, 1),
        ]

        for product_id, seller_id, quantity in examples:
            exists = (
                session.query(Sale)
                .filter(
                    Sale.product_id == product_id,
                    Sale.seller_id == seller_id,
                    Sale.quantity == quantity,
                )
                .first()
            )
            if not exists:
                session.add(Sale(product_id=product_id, seller_id=seller_id, quantity=quantity))

        session.commit()
        print("Sales inseridas/verificadas com sucesso!")
    except Exception as e:
        session.rollback()
        print("Erro ao inserir sales:", e)
        raise
    finally:
        session.close()

if __name__ == "__main__":
    seed_products()
    seed_sellers()
    seed_sales()


