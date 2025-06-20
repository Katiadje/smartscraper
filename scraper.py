import requests
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Dataset(Base):
    __tablename__ = 'datasets'

    id = Column(String(255), primary_key=True)  # id fourni par l'API (string)
    title = Column(String(255))
    description = Column(String(1024))
    url = Column(String(255))

    def __init__(self, id, title, description, url):
        self.id = id
        self.title = title
        self.description = description
        self.url = url

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "url": self.url
        }

# Configuration base de données selon ton docker-compose
DATABASE_URL = "mysql+pymysql://scraperuser:userpassword@db:3306/smartscraper"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def save_dataset(session, dataset: Dataset):
    existing = session.query(Dataset).filter(Dataset.id == dataset.id).first()
    if existing:
        # Optionnel : mettre à jour les champs si nécessaire
        existing.title = dataset.title
        existing.description = dataset.description
        existing.url = dataset.url
    else:
        session.add(dataset)

def scrape_data_gouv(page=1, page_size=20):
    url = f"https://www.data.gouv.fr/api/1/datasets/?page={page}&page_size={page_size}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        raw_data = response.json().get('data', [])

        datasets = []
        for item in raw_data:
            ds = Dataset(
                id=item.get('id'),
                title=item.get('title'),
                description=item.get('description'),
                url=item.get('page') or f"https://www.data.gouv.fr/fr/datasets/{item.get('id')}"
            )
            datasets.append(ds)

        # Sauvegarde en base
        session = SessionLocal()
        try:
            for ds in datasets:
                save_dataset(session, ds)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Erreur lors de la sauvegarde en base : {e}")
        finally:
            session.close()

        return datasets

    except requests.RequestException as e:
        print(f"Erreur lors du scraping : {e}")
        return []