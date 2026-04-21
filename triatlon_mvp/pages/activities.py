import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date


def render_activities():
    st.markdown("<div class='section-title'>Registro de actividades</div>", unsafe_allow_html=True)
    df = st.session_state.activities
    tab1, tab2 = st.tabs(["Registrar", "Histórico"])

    with tab1:
        c1, c2, c3 = st.columns(3)
        fecha = c1.date_input("Fecha", value=date.today())
        disciplina = c2.selectbox("Disciplina", ["Natación", "Ciclismo", "Carrera", "Fuerza"])
        estado = c3.selectbox("Estado", ["Completado", "Parcial", "Omitido"])
        sesion = st.text_input("Sesión")
        d1, d2, d3 = st.columns(3)
        duracion = d1.number_input("Duración (min)", min_value=0, max_value=500, value=50)
        distancia = d2.number_input("Distancia", min_value=0.0, max_value=300.0, value=10.0, step=0.1)
        rpe = d3.slider("RPE", 1, 10, 6)
        if st.button("Guardar actividad"):
            row = pd.DataFrame([{
                "Fecha": fecha, "Disciplina": disciplina, "Sesión": sesion, "Duración (min)": duracion,
                "Distancia": distancia, "RPE": rpe, "Estado": estado
            }])
            st.session_state.activities = pd.concat([st.session_state.activities, row], ignore_index=True)
            st.success("Actividad registrada")
            st.rerun()

    with tab2:
        st.dataframe(df.sort_values("Fecha", ascending=False), use_container_width=True, hide_index=True)
        weekly = df.groupby("Disciplina", as_index=False)["Distancia"].sum()
        fig = px.pie(weekly, values="Distancia", names="Disciplina", hole=.55, color_discrete_sequence=["#bb5cff", "#7f8cff", "#39d98a", "#ffb547"])
        fig.update_layout(height=340, paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#f4efff"))
        st.plotly_chart(fig, use_container_width=True)
