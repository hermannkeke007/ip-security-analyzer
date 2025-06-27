# IP Security Analyzer 🛡️

Un outil d'analyse de sécurité complet pour les adresses IP qui combine plusieurs sources de données et génère des rapports intelligents avec l'IA.

## 🚀 Fonctionnalités

- **Géolocalisation précise** : Localisation avec coordonnées GPS
- **Analyse de sécurité** : Vérification de réputation et détection de menaces
- **Ports ouverts** : Scan des services exposés via Shodan
- **Rapports IA** : Analyse intelligente générée par OpenAI
- **Visualisation** : Liens Google Maps cliquables
- **Interface moderne** : Interface web responsive avec Bootstrap

## 🔧 APIs Utilisées

- **ipinfo.io** : Géolocalisation de base (gratuit)
- **ip-api.com** : Informations détaillées de géolocalisation (gratuit)
- **AbuseIPDB** : Vérification de réputation et signalements d'abus
- **Shodan** : Scan des ports ouverts et services
- **OpenAI** : Génération de rapports intelligents

## 📋 Prérequis

1. Python 3.11+
2. Clés API (optionnelles mais recommandées) :
   - OpenAI API Key
   - AbuseIPDB API Key
   - Shodan API Key

## 🛠️ Installation

### 1. Cloner le repository

```bash
git clone https://github.com/votre-username/ip-security-analyzer.git
cd ip-security-analyzer
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configuration des variables d'environnement

```bash
# Copier le fichier d'exemple
cp .env.example .env

# Éditer le fichier .env avec vos clés API
nano .env
```

Exemple de fichier `.env` :
```
OPENAI_API_KEY=sk-your-openai-key-here
ABUSEIPDB_API_KEY=your-abuseipdb-key-here
SHODAN_API_KEY=your-shodan-key-here
FLASK_ENV=production
```

### 4. Lancer l'application

```bash
# En local
python app.py

# Ou avec gunicorn (production)
gunicorn --bind 0.0.0.0:5000 app:app
```

L'application sera accessible sur `http://localhost:5000`

## 🚀 Déploiement

### Railway (Recommandé)

1. **Créer un compte sur [Railway](https://railway.app)**

2. **Connecter votre repository GitHub**
   ```bash
   # Pousser le code sur GitHub
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

3. **Déployer sur Railway**
   - Aller sur Railway Dashboard
   - Cliquer sur "New Project"
   - Sélectionner "Deploy from GitHub repo"
   - Choisir votre repository

4. **Configurer les variables d'environnement**
   - Aller dans l'onglet "Variables"
   - Ajouter vos clés APIs :
     - `OPENAI_API_KEY`
     - `ABUSEIPDB_API_KEY`
     - `SHODAN_API_KEY`

### AWS (Alternative)

1. **Utiliser AWS Elastic Beanstalk**
   ```bash
   # Installer EB CLI
   pip install awsebcli

   # Initialiser
   eb init -p python-3.11 ip-security-analyzer

   # Créer l'environnement
   eb create production

   # Configurer les variables d'environnement
   eb setenv OPENAI_API_KEY=your-key ABUSEIPDB_API_KEY=your-key SHODAN_API_KEY=your-key

   # Déployer
   eb deploy
   ```

2. **Ou utiliser Docker avec ECS**
   ```bash
   # Build l'image
   docker build -t ip-security-analyzer .

   # Tester localement
   docker run -p 5000:5000 --env-file .env ip-security-analyzer
   ```

## 📖 Utilisation

### Interface Web

1. Ouvrir l'application dans votre navigateur
2. Entrer une adresse IP (ex: 8.8.8.8)
3. Cliquer sur "Analyser"
4. Consulter le rapport généré

### Exemple d'analyse

L'application fournit :
- **Localisation** : Pays, ville, coordonnées GPS
- **Informations techniques** : ISP, organisation, type d'hébergement
- **Sécurité** : Score de réputation, signalements d'abus
- **Services** : Ports ouverts, services détectés
- **Rapport IA** : Analyse intelligente des risques
- **Carte** : Lien vers Google Maps avec la localisation

## 🔐 Sécurité

- Les clés API sont stockées de manière sécurisée dans les variables d'environnement
- Le fichier `.env` est exclu du versioning via `.gitignore`
- L'application valide les formats d'adresses IP
- Timeout configuré pour toutes les requêtes API

## 🛡️ APIs Gratuites vs Payantes

### Gratuites (fonctionnent sans clé)
- **ipinfo.io** : 50,000 requêtes/mois
- **ip-api.com** : 1,000 requêtes/mois

### Nécessitent une clé API
- **AbuseIPDB** : 1,000 requêtes/jour (gratuit)
- **Shodan** : 100 requêtes/mois (gratuit)
- **OpenAI** : Pay-as-you-go (quelques centimes par rapport)

## 📁 Structure du Projet

```
ip-security-analyzer/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── Dockerfile            # Configuration Docker
├── railway.json          # Configuration Railway
├── .env.example          # Exemple de variables d'environnement
├── .gitignore           # Fichiers à ignorer
├── templates/
│   └── index.html       # Interface web
└── README.md           # Documentation
```

## 🚨 Gestion d'Erreurs

L'application gère automatiquement :
- **APIs indisponibles** : Continue avec les autres sources
- **Clés manquantes** : Fonctionne en mode dégradé
- **Timeouts** : Évite les blocages
- **IPs invalides** : Validation côté client et serveur

## 🔄 Améliorations Futures

- [ ] Cache Redis pour améliorer les performances
- [ ] Base de données pour historique des analyses
- [ ] API REST pour intégrations tierces
- [ ] Notifications par email pour IPs suspectes
- [ ] Dashboard administrateur
- [ ] Support IPv6
- [ ] Intégration Slack/Discord

## 📞 Support

Pour obtenir vos clés API :

1. **OpenAI** : https://platform.openai.com/api-keys
2. **AbuseIPDB** : https://www.abuseipdb.com/api
3. **Shodan** : https://developer.shodan.io/api

## 📄 Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Créer une Pull Request

---

**⚠️ Avertissement** : Cet outil est destiné à des fins éducatives et de sécurité légitimes. Respectez les conditions d'utilisation de toutes les APIs utilisées.