# Image de base
FROM python:3.10-slim

# Dossier de travail
WORKDIR /app

# Copier les fichiers du backend
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Lancer l'app Flask
CMD ["python", "app.py"]
