import pandas as pd
import plotly.express as px

chuva_ou_sol = [
    1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,
    1,1,1,
    0,0,0,0,
    0,1,1,1,1,1,1,
    0,0,0
]

df = pd.DataFrame({
    "Dia": list(range(1, 32)),
    "Estado": chuva_ou_sol
})

df["Clima"] = df["Estado"].map({1: "Chuva", 0: "Sol"})

dias_chuva = df["Clima"].value_counts()["Chuva"]
dias_sol = df["Clima"].value_counts()["Sol"]

print(f"Dias de chuva: {dias_chuva}")
print(f"Dias de sol: {dias_sol}")


fig = px.bar(
    df,
    x="Dia",
    y=[1]*len(df), 
    color="Clima",
    color_discrete_map={
        "Chuva": "#C00000",  
        "Sol": "#FFF59D"     
    },
    title="Janeiro 2026 — Distribuição de Dias de Chuva e Sol",
)

fig.update_layout(
    template="simple_white",
    showlegend=True,
    font=dict(family="Georgia", size=14),
    title_font=dict(size=20),
    xaxis_title="Dia do Mês",
    yaxis_visible=False,
    plot_bgcolor="white"
)

fig.update_traces(
    hovertemplate="<b>Dia %{x}</b><br>Clima: %{marker.color}<extra></extra>"
)

fig.show()
