#!/bin/bash

echo "🚀 Configuration de IP Security Analyzer"
echo "========================================"

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    exit 1
fi

echo "✅ Python détecté: $(python3 --version)"

# Créer l'environnement virtuel
echo "📦 Création de l'environnement virtuel..."
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
echo "📥 Installation des dépendances..."
pip install -r requirements.txt

# Créer le fichier .env
if [ ! -f .env ]; then
    echo "⚙️ Création du fichier .env..."
    cp .env.example .env
    echo "✏️ Veuillez éditer le fichier .env avec vos clés API"
    echo "   nano .env"
else
    echo "✅ Fichier .env déjà existant"
fi

# Créer le dossier templates s'il n'existe pas
mkdir -p templates

echo ""
echo "🎉 Installation terminée !"
echo ""
echo "Prochaines étapes :"
echo "1. Éditer le fichier .env avec vos clés API"
echo "2. Lancer l'application : python app.py"
echo "3. Ouvrir http://localhost:5000 dans votre navigateur"
echo ""
echo "Pour le déploiement :"
echo "- Railway : Pousser sur GitHub et connecter à Railway"
echo "- AWS : Utiliser Elastic Beanstalk ou ECS"
echo ""