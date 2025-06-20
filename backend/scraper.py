import requests

class Dataset:
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

def scrape_data_gouv(page=1, page_size=20):
    """
    Récupère la liste des jeux de données depuis l'API data.gouv.fr,
    avec pagination.
    """
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

        return datasets

    except requests.RequestException as e:
        print(f"Erreur lors du scraping : {e}")
        return []
