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

### 4. Lancer l'application

```bash
# En local
python app.py

# Ou avec gunicorn (production)
gunicorn --bind 0.0.0.0:5000 app:app
```

L'application sera accessible sur `http://localhost:5000`


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
