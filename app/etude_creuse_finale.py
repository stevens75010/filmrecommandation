import streamlit as st
import pandas as pd
import plotly.express as px

# 🔢 Données population
pop = {
    'Territoire': ['Creuse', 'Nouvelle-Aquitaine', 'Île-de-France'],
    'Population': [115529, 6191209, 12278210]
}

st.subheader("Population en 2022")
df_pop = pd.DataFrame(pop)
fig_pop = px.bar(df_pop, x='Territoire', y='Population',
                 title="Population (2022)",
                 text='Population')
fig_pop.update_traces(texttemplate='%{text:,}', textposition='outside')
st.plotly_chart(fig_pop, use_container_width=True)

# 🍰 Répartition par âge
st.subheader("Structure d'âge – Comparatif")

ages = ['<20', '20-59', '60-75', '75+']
creuse = [20297, 47419, 28025, 18362]
na = [1273349, 2910151, 1218179, 789530]
idf = []  # remplacer si dispo

# Camembert Creuse
df_age_creuse = pd.DataFrame({'Tranche': ages, 'Population': creuse})
fig_age_c = px.pie(df_age_creuse, names='Tranche', values='Population',
                   title="Creuse – par tranche d’âge")
st.plotly_chart(fig_age_c, use_container_width=True)

# Barres comparatives Creuse vs Nouvelle-Aquitaine
df_age_cmp = pd.DataFrame({
    'Tranche': ages * 2,
    'Territoire': ['Creuse']*4 + ['Nouvelle-Aquitaine']*4,
    'Population': creuse + na
})
fig_age_cmp = px.bar(df_age_cmp, x='Tranche', y='Population', color='Territoire',
                     barmode='group',
                     title="Répartition des âges : Creuse vs Nouvelle-Aquitaine")
st.plotly_chart(fig_age_cmp, use_container_width=True)

# 🎬 Cinéma : Estimations séances/entrées (créneaux fictifs)
st.subheader("Cinéma – Estimations séances et fréquentation")

data_cinema = {
    'Année': [2010, 2015, 2022],
    'Creuse Séances': [6000, 5500, 5800],
    'NA Séances': [200000, 210000, 220000],  # à ajuster
    'NA Entrées': [4000000, 4200000, 4400000],
    'IDF Séances': [400000, 430000, 460000],
    'IDF Entrées': [8000000, 8500000, 9000000]
}
df_cinema = pd.DataFrame(data_cinema)

df_m = df_cinema.melt(id_vars='Année', var_name='Territoire-Indicateur', value_name='Valeur')
df_m[['Territoire', 'Indicateur']] = df_m['Territoire-Indicateur'].str.split(' ', expand=True)

fig_cinema = px.bar(df_m, x='Année', y='Valeur', color='Territoire',
                    facet_col='Indicateur', barmode='group',
                    title="Séances et Entrées (évol. 2010‑2022)")
st.plotly_chart(fig_cinema, use_container_width=True)

# 🔢 Taux de remplissage et entrées par habitant (2022)
st.subheader("Indicateurs 2022")

# Hypothèse : capacité moyenne 100 places/séance
indicators = []
for terr, séances, entrées, popu in [
    ('Creuse', 5800, 140000, 115529),
    ('Nouvelle-Aquitaine', 220000, 4400000, 6191209),
    ('Île-de-France', 460000, 9000000, 12278210)
]:
    cap = séances * 100
    taux = entrées / cap * 100
    entr_hab = entrées / popu
    indicators.append({
        'Territoire': terr,
        'Taux remplissage (%)': round(taux,1),
        'Entrées / hab.': round(entr_hab,3)
    })

df_ind = pd.DataFrame(indicators)
st.table(df_ind.style.format({'Taux remplissage (%)':'{:.1f}','Entrées / hab.':'{:.3f}'}))
