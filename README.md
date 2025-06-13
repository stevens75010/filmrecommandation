# 🎬 Ma Plateforme VOD – Un Netflix éducatif & data-driven

Bienvenue sur ma plateforme VOD développée avec **Streamlit** dans le cadre d'un projet de data analyse et data engineering.

---

## 🌐 Démo en ligne

🔗 [Lien vers l'application Streamlit](https://)

---

## 🎯 Objectifs

- Explorer un catalogue de films interactif à la manière de Netflix
- Visualiser les tendances cinématographiques (genres, durée, notes)
- Recommander des films personnalisés via un système de similarité
- Analyser le territoire (ici : La Creuse) et adapter l’offre au public cible

---

## 🚀 Fonctionnalités

- 🖼️ Interface visuelle type Netflix avec affiches
- 🔎 Recherche par titre, genre, note, durée
- 📊 Visualisations interactives (bar, pie, treemap, line)
- 🤖 Recommandation de films avec KNN
- 🌍 Intégration API TMDb (affiches, trailers)
- 🎯 KPI et analyse territoriale via données INSEE

---

## 🛠️ Stack technique

| Outil / Lib         | Rôle                             |
|---------------------|----------------------------------|
| `streamlit`         | Interface web                    |
| `pandas`, `numpy`   | Manipulation de données          |
| `plotly`, `seaborn` | Visualisations                   |
| `scikit-learn`      | Algorithme KNN                   |
| `requests`          | Appels API (TMDb, OMDb)          |
| `st-echarts`, `st-clickable-images` | UI avancée      |

---

## 📂 Structure du projet

```
ma-plateforme-vod/
├── 📁 data/                        # Données sources
│   ├── df_imdb_final.csv          # Fichier final utilisé dans l'app
│   └── autres_fichiers.csv        # (ex: fichier réalisateurs populaires)
│
├── 📁 assets/                     # Images, logos, graphiques
│   ├── evol_repa_ages.png
│   └── autres_images.png
│
├── 📁 app/                        # Code principal de l'application
│   ├── streamlit_app.py          # L'application principale (le fichier que tu m'as donné)
│   ├── utils.py                  # Fonctions utilitaires (API, formatage, cache…)
│   └── styles.css                # CSS personnalisé (si tu veux externaliser)
│
├── 📁 notebooks/                 # Jupyter notebooks pour l'exploration ou l'analyse
│   └── analyse_initiale.ipynb
│
├── 📁 ressources/                # Docs externes, cahier des charges, notes
│   └── presentation_projet.md
│
├── requirements.txt              # Dépendances Python
├── README.md                     # Présentation du projet
```

---

## 🧪 Tests

Un jeu de tests simples est inclus dans le dossier `tests/`, à exécuter avec :

```bash
pytest tests/
```

---

## 🐳 Déploiement avec Docker

```Dockerfile
# Dockerfile simple pour Streamlit
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Pour construire et lancer :

```bash
docker build -t plateforme-vod .
docker run -p 8501:8501 plateforme-vod
```

---

## 👥 Auteurs

Projet réalisé à la **Wild Code School 2025**  
Équipe : Zyed, Stevens, Christopher, Alexis
