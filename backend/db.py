from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://scraperuser:userpassword@db:3306/smartscraper")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class DatasetDB(Base):
    __tablename__ = 'datasets'

    id = Column(String, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    url = Column(String(255))
