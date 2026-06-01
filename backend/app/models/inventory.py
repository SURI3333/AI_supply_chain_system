from sqlalchemy import Column, Integer, Float, String
from app.config.database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    product_id = Column(String)
    warehouse_id = Column(String)
    sales = Column(Float)
    stock = Column(Float)

Base.metadata.create_all(bind=engine)