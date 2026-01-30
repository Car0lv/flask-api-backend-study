from sqlalchemy import Column, Integer, String
from database.connection import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)

    sales = relationship("Sale", back_populates="product")

    def __repr__(self):
        return f"<Product id={self.id} name={self.name}>"
