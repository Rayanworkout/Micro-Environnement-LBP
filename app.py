import pandas as pd
import plotly.express as px
import streamlit as st


# QUANTIFICATION DE LA CIBLE (POTENTIEL DE MARCHÉ, NOMBRE DE GENS EN CLASSE MOYENNE PAR EXEMPLE)
# CRÉER UN PERSONA

st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="🧊")


st.image("logos/siege_lbp.jpg", width=900)

with open("text/part1.md") as file:
    text = file.read()

st.markdown(text, unsafe_allow_html=True)


# st.sidebar.title("À l'attention de Moracchioli Franck")
# st.sidebar.write("de Mokrane Rayan")
# st.sidebar.write("Code Source https://github.com/Rayanworkout/Micro-Environnement-LBP")


st.image("logos/concurrents_directs.png", width=900)

with open("text/part2.md") as file:
    text = file.read()

st.markdown(text, unsafe_allow_html=True)


# FIN PARTIE 2

with open("text/part3.md") as file:
    text = file.read()

st.markdown(text, unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.image("logos/binance.png")

with col2:
    st.image("logos/kraken.png")

with col3:
    st.image("logos/coinbase.png")


# FIN PARTIE 3

with open("text/part4.md") as file:
    text = file.read()

st.markdown(text, unsafe_allow_html=True)

data1 = [
    ["Services en Ligne", "Innovation", "Positionnement international"],
    {"Établissement": "La Banque Postale", "x": 6, "y": 5.3, "z": 4},
    {"Établissement": "BNP Paribas", "x": 7.8, "y": 8.8, "z": 8.5},
    {"Établissement": "Crédit Agricole", "x": 5, "y": 6.9, "z": 6.3},
    {"Établissement": "Société Générale", "x": 6.1, "y": 7.4, "z": 7.2},
    {"Établissement": "Crédit Mutuel", "x": 7, "y": 7.1, "z": 7.8},
    {"Établissement": "Boursorama", "x": 9.7, "y": 7.7, "z": 6.4},
    {"Établissement": "Hello Bank", "x": 9.6, "y": 7.6, "z": 6.5},
    {"Établissement": "ING Direct", "x": 9.5, "y": 7.5, "z": 6.6},
    {"Établissement": "BforBank", "x": 9.4, "y": 5.5, "z": 6.7},
    {"Établissement": "N26", "x": 9.3, "y": 7.8, "z": 7},
    {"Établissement": "Revolut", "x": 9.2, "y": 8, "z": 7.3},
    {"Établissement": "HSBC", "x": 8.5, "y": 8.3, "z": 7.4},
    {"Établissement": "LCL", "x": 6.5, "y": 8.4, "z": 7.5},
    {"Établissement": "CIC", "x": 7.5, "y": 5, "z": 7.6},
]


data2 = [
    ["Tarifs / Frais", "Maillage Territorial", "Satisfaction Client / Réputation"],
    {"Établissement": "La Banque Postale", "x": 6.8, "y": 8.6, "z": 4.5},
    {"Établissement": "BNP Paribas", "x": 5.2, "y": 7.3, "z": 9},
    {"Établissement": "Crédit Agricole", "x": 4.6, "y": 8, "z": 6.1},
    {"Établissement": "Société Générale", "x": 6.1, "y": 8.4, "z": 7.2},
    {"Établissement": "Crédit Mutuel", "x": 7.1, "y": 6, "z": 8.8},
    {"Établissement": "Boursorama", "x": 8.5, "y": 0, "z": 8},
    {"Établissement": "Hello Bank", "x": 8.2, "y": 0, "z": 7.2},
    {"Établissement": "ING Direct", "x": 7.9, "y": 0, "z": 6.8},
    {"Établissement": "BforBank", "x": 7.8, "y": 0, "z": 7.4},
    {"Établissement": "N26", "x": 8.6, "y": 0, "z": 8},
    {"Établissement": "Revolut", "x": 8.5, "y": 0, "z": 9},
    {"Établissement": "HSBC", "x": 6.3, "y": 7.3, "z": 6.6},
    {"Établissement": "LCL", "x": 4.8, "y": 8.1, "z": 7.3},
    {"Établissement": "CIC", "x": 5, "y": 8.4, "z": 4},
]

df1 = pd.DataFrame(data1[1:])
df2 = pd.DataFrame(data2[1:])

df1.rename(
    {"x": "Services en Ligne", "y": "Innovation", "z": "Positionnement international"},
    axis=1,
    inplace=True,
)

df2.rename(
    {
        "x": "Tarifs / Frais",
        "y": "Maillage Territorial",
        "z": "Satisfaction Client / Réputation",
    },
    axis=1,
    inplace=True,
)


fig1 = px.scatter_3d(
    df1,
    title="📊 Innovation, Services en Ligne et Positionnement International",
    x="Services en Ligne",
    y="Innovation",
    z="Positionnement international",
    text="Établissement",
    size_max=18,
    color="Établissement",
    color_discrete_map={"La Banque Postale": "blue"},
    opacity=0.7,
    template="seaborn",
    height=900,
    width=1000,
)

fig2 = px.scatter_3d(
    df2,
    title="📊 Tarifs, Maillage Territorial et Satisfaction Client",
    x="Tarifs / Frais",
    y="Maillage Territorial",
    z="Satisfaction Client / Réputation",
    text="Établissement",
    size_max=18,
    color="Établissement",
    color_discrete_map={"La Banque Postale": "blue"},
    opacity=0.7,
    template="seaborn",
    height=900,
    width=1000,
)

st.plotly_chart(fig1)
st.plotly_chart(fig2)


# FIN PARTIE 4

with open("text/part5.md") as file:
    text = file.read()

st.markdown(text, unsafe_allow_html=True)

st.image("logos/bnp.png", width=700)


# FIN PARTIE 5

with open("text/part6.md") as file:
    text = file.read()

st.markdown(text, unsafe_allow_html=True)

st.image("logos/porter.png", width=700)


# FIN PARTIE 6

with open("text/part7.md") as file:
    text = file.read()

st.markdown(text, unsafe_allow_html=True)

st.image("logos/clients.png", width=700)

# FIN PARTIE 7

with open("text/part8.md") as file:
    text = file.read()

st.markdown(text, unsafe_allow_html=True)