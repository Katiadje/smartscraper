from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connexion MySQL
DB_USER = 'scraperuser'
DB_PASSWORD = 'userpassword'
DB_HOST = 'db'  # Nom du service dans docker-compose
DB_PORT = '3306'
DB_NAME = 'smartscraper'

DATABASE_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Créer l'engine
engine = create_engine(DATABASE_URL, echo=True)

# Créer la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
