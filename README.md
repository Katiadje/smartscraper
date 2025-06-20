# 📊 SmartScraper - Scraping des jeux de données de data.gouv.fr

## 🧩 Description

SmartScraper est une application web Flask qui permet de :
- Scraper des jeux de données depuis l'API officielle de [data.gouv.fr](https://www.data.gouv.fr/api/1/datasets/)
- Persister ces jeux de données dans une base MySQL
- Fournir une API REST pour interagir avec les données
- Visualiser les données via une interface web

## 🌟 Fonctionnalités

### 🕷️ Module de scraping
- Récupération des métadonnées des datasets
- Filtrage par thématique/organisation
- Mise à jour incrémentale

### 🗃️ Persistance des données
- Modèle relationnel complet
- Historique des versions
- Recherche full-text

### 🔌 API REST
- CRUD complet
- Pagination
- Filtres avancés

## 📦 Architecture du projet

```plaintext
smartscraper/
│
├── backend/
│   ├── app.py            # Serveur Flask et routes API
│   ├── db.py             # Connexion SQLAlchemy et modèle DatasetDB
│   ├── scraper.py        # Scraper de l'API data.gouv.fr
│   ├── services/         # Logique métier
│   ├── config.py         # Configuration
│   └── requirements.txt  # Dépendances Python
│
├── frontend/             # Interface React
│   ├── public/
│   └── src/
│       ├── components/   # Composants React
│       └── api/          # Clients API
│
├── docker/
│   ├── mysql/            # Config MySQL
│   └── nginx/            # Config reverse proxy
│
├── docker-compose.yml    # Orchestration des services
└── README.md             # Documentation