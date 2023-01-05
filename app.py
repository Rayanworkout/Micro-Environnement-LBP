import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Comparatif des banques en ligne")

with open("data.md", "r") as readme:
    text = readme.read()
    
st.markdown(text)


data = [
    [
        ["Services en Ligne", "Innovation", "Positionnement international"],
        {"label": "La Banque Postale", "x": 6, "y": 5.3, "z": 4},
        {"label": "BNP Paribas", "x": 7.8, "y": 8.8, "z": 8.5},
        {"label": "Crédit Agricole", "x": 5, "y": 6.9, "z": 6.3},
        {"label": "Société Générale", "x": 6.1, "y": 7.4, "z": 7.2},
        {"label": "Crédit Mutuel", "x": 7, "y": 7.1, "z": 7.8},
        {"label": "Boursorama", "x": 9.7, "y": 7.7, "z": 6.4},
        {"label": "Hello Bank", "x": 9.6, "y": 7.6, "z": 6.5},
        {"label": "ING Direct", "x": 9.5, "y": 7.5, "z": 6.6},
        {"label": "BforBank", "x": 9.4, "y": 5.5, "z": 6.7},
        {"label": "N26", "x": 9.3, "y": 7.8, "z": 7},
        {"label": "Revolut", "x": 9.2, "y": 8, "z": 7.3},
        {"label": "HSBC", "x": 8.5, "y": 8.3, "z": 7.4},
        {"label": "LCL", "x": 6.5, "y": 8.4, "z": 7.5},
        {"label": "CIC", "x": 7.5, "y": 5, "z": 7.6},
    ],
    [
        ["Tarifs / Frais", "Maillage Territorial", "Satisfaction Client / Réputation"],
        {"label": "La Banque Postale", "x": 6.8, "y": 8.6, "z": 4.5},
        {"label": "BNP Paribas", "x": 5.2, "y": 7.3, "z": 9},
        {"label": "Crédit Agricole", "x": 4.6, "y": 8, "z": 6.1},
        {"label": "Société Générale", "x": 6.1, "y": 8.4, "z": 7.2},
        {"label": "Crédit Mutuel", "x": 7.1, "y": 6, "z": 8.8},
        {"label": "Boursorama", "x": 8.5, "y": 0, "z": 8},
        {"label": "Hello Bank", "x": 8.2, "y": 0, "z": 7.2},
        {"label": "ING Direct", "x": 7.9, "y": 0, "z": 6.8},
        {"label": "BforBank", "x": 7.8, "y": 0, "z": 7.4},
        {"label": "N26", "x": 8.6, "y": 0, "z": 8},
        {"label": "Revolut", "x": 8.5, "y": 0, "z": 9},
        {"label": "HSBC", "x": 6.3, "y": 7.3, "z": 6.6},
        {"label": "LCL", "x": 4.8, "y": 8.1, "z": 7.3},
        {"label": "CIC", "x": 5, "y": 8.4, "z": 4},
    ],
]

for element in data:
    df = pd.DataFrame(element[1:])
    
    fig = px.scatter_3d(
        df, x="x", y="y", z="z", text="label", color="label", size_max=18, opacity=0.7
    )  

    st.plotly_chart(fig)
