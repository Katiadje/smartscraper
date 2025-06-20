from sqlalchemy import Column, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dataset(Base):
    __tablename__ = 'datasets'

    id = Column(String, primary_key=True)          # L'id est une string (car souvent API renvoie un id textuel)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    url = Column(String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "url": self.url
        }
