from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

Base = declarative_base()

class DatasetDB(Base):
    __tablename__ = 'datasets'

    id = Column(String(255), primary_key=True)
    title = Column(String(255))
    description = Column(String(1024))
    url = Column(String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
        }

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://scraperuser:userpassword@db:3306/smartscraper")
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Création des tables (faire une seule fois ici)
Base.metadata.create_all(engine)
