from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey("sellers.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="sales")
    seller = relationship("Seller", back_populates="sales")

    def __repr__(self):
        return (
            f"<Sale id={self.id} product_id={self.product_id} "
            f"seller_id={self.seller_id} quantity={self.quantity}>"
        )
