FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Créer le dossier templates s'il n'existe pas
RUN mkdir -p templates

# Exposer le port
EXPOSE 5000

# Commande par défaut
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]