from sqlalchemy import Column, Integer, String
from database.connection import Base
from sqlalchemy.orm import relationship


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)

    sales = relationship("Sale", back_populates="seller")  
     
    def __repr__(self):
        return f"<Seller id={self.id} name={self.name}>"
