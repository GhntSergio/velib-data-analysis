# Analyse des données Vélib en temps réel 🚲📊

> 🇬🇧 **English summary:** Real-time monitoring and analysis of Paris Vélib' bike-sharing data: API extraction, CSV storage, alerts on empty stations and interactive Matplotlib/Folium visualizations. Available on PyPI as `velib-monitoring`.

## Description
Ce projet permet d'explorer et d'analyser les données en temps réel du service Vélib' à Paris.
Il comprend :
- **Extraction des données** en temps réel depuis l'API Vélib.
- **Stockage des données** dans un fichier CSV.
- **Surveillance des stations** pour détecter les vélos disponibles.
- **Visualisation interactive** des données avec Matplotlib et Folium.

## Installation via PyPI 🛠️
Vous pouvez installer ce package directement depuis PyPI :
```sh
pip install velib-monitoring
```

## Utilisation 🚀
### 1️⃣ Exécuter la commande de surveillance des vélos :
Après l'installation, vous pouvez lancer la surveillance des stations Vélib avec :
```sh
velib-monitor
```
Ce script récupère les données en temps réel, les stocke dans un fichier CSV et surveille les stations sans vélos.

### 2️⃣ Ouvrir le notebook de visualisation :
Lancer Jupyter Notebook et exécuter les analyses interactives :
```sh
jupyter notebook notebooks/velib_visualisation.ipynb
```

## Structure du projet 📁
```
velib-data-analysis/
│── data/                 # Stockage des fichiers CSV et autres données brutes
│   ├── velib_data.csv    
│
│── logs/
│   ├── velib_monitoring.log    
│── notebooks/            # Notebooks Jupyter pour l'analyse et visualisation
│   ├── velib_visualisation.ipynb
│
│── velib_data_analysis/   # 🔹 Le package Python & Scripts Python pour extraction et surveillance
│   ├── __init__.py        # 🔹 pour le package
│   ├── velib_monitoring.py
│
│── docs/                 # Documentation du projet (README, notes, etc.)
│   ├── README.md
│
│── requirements.txt      # Liste des dépendances Python
│── .gitignore            # Exclusion des fichiers inutiles
│── LICENSE               # Licence du projet
│── setup.py              # projet en package Python
```

## Technologies utilisées 🛠️
- **Python** (requests, pandas, seaborn, matplotlib, folium)
- **Jupyter Notebook** pour l'analyse interactive
- **API OpenDataSoft** pour l'accès aux données Vélib

## Améliorations possibles 🚀
- Ajouter des notifications par e-mail ou Telegram
- Héberger une application web pour suivre les vélos en direct
- Optimiser le stockage et l'analyse des données

## Licence 📜
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

✉️ **Contact & Contributions**
Si vous avez des idées d'amélioration ou des suggestions, n'hésitez pas à créer une *issue* ou une *pull request* sur le dépôt GitHub ! 😊
