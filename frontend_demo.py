import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="5SensAI Dashboard", layout="wide")

# Estilo Titanium (Simplificado para Demo)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("⛩️ 5SensAI - Dashboard de Auditoria (Demo)")

# Carregar dados locais
df = pd.read_csv("exemplo_dados.csv")

# KPIs Rápidos
col1, col2, col3 = st.columns(3)
col1.metric("Total de Auditorias", len(df))
col2.metric("Conformidade", f"{(df['Classificacao'] == 'Conforme').mean()*100:.0f}%")
col3.metric("Senso Crítico", "Seiri")

st.divider()

# Gráfico de Barras por Senso
st.subheader("Distribuição por Senso 5S")
fig = px.bar(df, x="Senso_Sugerido", color="Classificacao", barmode="group",
             color_discrete_map={"Conforme": "#2ecc71", "Não Conforme": "#e74c3c"})
st.plotly_chart(fig, use_container_width=True)

st.table(df)