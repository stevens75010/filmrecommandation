🎬 Ma Plateforme VOD : un Netflix éducatif & data-driven
Bienvenue sur ma plateforme VOD développée avec Streamlit dans le cadre d'un projet de data analyse & data engineering.

🎯 Objectif du projet
Créer une application inspirée de Netflix permettant :

d'explorer un vaste catalogue de films issus d’IMDb

de visualiser les tendances cinématographiques

de générer des recommandations intelligentes basées sur les goûts utilisateurs

🚀 Fonctionnalités principales
Fonction	Description
🖼️ Interface Netflix	Affichage élégant des films sous forme de "cartes" avec affiches, notes, synopsis
🔎 Recherche & filtres	Par titre, genre, décennie, acteur, réalisateur
📊 Visualisation	Genres les plus présents, durée moyenne, acteurs populaires, notes IMDb
🤖 Recommandation	Moteur KNN basé sur la similarité de genres, réalisateurs et acteurs
🌐 API externes	TMDb (affiches, résumés, trailers), IMDb, OMDb
🎨 UI enrichie	CSS customisé, icônes, sidebar dynamique, transitions animées

🛠️ Technologies utilisées
Technologie	Rôle
streamlit	Interface web rapide en Python
pandas, numpy	Manipulation et traitement de données
plotly, seaborn, matplotlib	Visualisations interactives et statistiques
requests	Appels API (TMDb, OMDb)
streamlit-lottie, streamlit-echarts, st-clickable-images, st_on_hover_tabs	Widgets interactifs, animations, effets visuels
scikit-learn	Modèle KNN de recommandation

🔍 Décryptage du code Streamlit
🧱 1. Structure principale
st.set_page_config(page_title="WMDb", layout="wide")

➡️ Configure la page (titre, icône, largeur).

🧭 2. Navigation via sidebar customisée
python
Copier
Modifier
selected = on_hover_tabs(tabName=[...], iconName=[...])
➡️ Permet de naviguer dans les sections (Accueil, Notre démarche, Le cinéma dans la Creuse…) avec un effet de survol stylé. Très intuitif pour l'utilisateur.

🧠 3. Chargement intelligent des données
python
Copier
Modifier
@st.cache_data
def load_data():
    return pd.read_csv("df_imdb_final.csv")
➡️ Fonction cache pour éviter de recharger à chaque fois le CSV principal nettoyé.

🖼️ 4. Affichage de films sous forme de carte HTML/CSS
python
Copier
Modifier
card_html = f\"\"\"
<div class='film-card'>
    <img src='{poster_url}'>
    <div class='film-info'>
        <div class='film-title'>{title}</div>
        ...
\"\"\"
➡️ Utilisation de HTML et CSS intégrés dans Streamlit pour créer une interface élégante type Netflix, avec :

📸 L’affiche du film

⭐ Note, votes, date de sortie

🧾 Résumé

🔗 Bande-annonce via TMDb API

🔢 5. Visualisations de données
python
Copier
Modifier
fig = px.treemap(...)
fig2 = px.bar(...)
fig4 = px.sunburst(...)
➡️ Analyse exploratoire sur :

📚 Répartition des genres

⏱️ Durée moyenne par genre

🎬 Réalisateurs et acteurs les plus populaires

❤️ 6. Recommandations personnalisées (KNN simplifié)
python
Copier
Modifier
if selected_title:
    recommended = df.copy()
    ...
    recommended = recommended.sort_values(by=["common_genres", "averageRating"])
➡️ Système de recommandation basé sur la similitude de genres, acteurs et réalisateurs avec pondération sur la note IMDb.

📦 7. API TMDb intégrée
python
Copier
Modifier
url = f"{BASE_URL}/movie/popular"
poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
➡️ Récupère les affiches, les résumés et les trailers des films grâce à l’API TMDb (api.themoviedb.org), avec gestion d’erreurs.

✅ Points forts
Très bonne séparation logique (onglets : contenu, data, recommandations)

Interface intuitive et moderne

Réelle valeur ajoutée pour un utilisateur final ou un cinéma local

Équilibre entre data science, visualisation, UX/UI et produit final fonctionnel

## 👨‍💻 Auteurs
Stevens, Christopher, Alexis, Zyed — Promo Wild Code School 2025
