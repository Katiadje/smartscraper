import requests
from db import DatasetDB, SessionLocal  # Import du vrai modèle et de la session
from sqlalchemy.exc import SQLAlchemyError

def save_dataset(session, dataset: DatasetDB):
    existing = session.query(DatasetDB).filter(DatasetDB.id == dataset.id).first()
    if existing:
        print(f"Dataset {dataset.id} déjà présent, mise à jour.")
        existing.title = dataset.title
        existing.description = dataset.description
        existing.url = dataset.url
    else:
        print(f"Ajout du dataset {dataset.id}")
        session.add(dataset)

def scrape_data_gouv(page=1, page_size=20):
    url = f"https://www.data.gouv.fr/api/1/datasets/?page={page}&page_size={page_size}"
    print(f"Requête envoyée à : {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()

        raw_data = response.json().get('data', [])
        print(f"Nombre d'éléments reçus : {len(raw_data)}")

        datasets = []
        for item in raw_data:
            ds = DatasetDB(
                id=item.get('id'),
                title=item.get('title'),
                description=item.get('description'),
                url=item.get('page') or f"https://www.data.gouv.fr/fr/datasets/{item.get('id')}"
            )
            datasets.append(ds)

        print(f"{len(datasets)} datasets prêts à être insérés")

        session = SessionLocal()
        try:
            for ds in datasets:
                save_dataset(session, ds)
            session.commit()
            print("Sauvegarde réussie en base de données.")
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Erreur lors de la sauvegarde en base : {e}")
        finally:
            session.close()

        return datasets

    except requests.RequestException as e:
        print(f"Erreur lors du scraping (réseau/API) : {e}")
        return []

    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return []
