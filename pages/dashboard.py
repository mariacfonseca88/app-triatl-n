import streamlit as st
import plotly.express as px
import pandas as pd


def render_dashboard():
    st.markdown("<div class='section-title'>Dashboard del atleta</div>", unsafe_allow_html=True)
    df = st.session_state.activities.copy()
    total_hours = round(df["Duración (min)"].sum() / 60, 1)
    total_sessions = len(df)
    compliance = 86
    ctl = 74
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Horas acumuladas", f"{total_hours} h", "+1.8")
    c2.metric("Sesiones", total_sessions, "+2")
    c3.metric("Cumplimiento", f"{compliance}%", "+4%")
    c4.metric("Fitness", ctl, "+3")

    left, right = st.columns([1.25, 0.75], gap="large")
    with left:
        by_day = pd.DataFrame({
            "Día": ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
            "Carga": [48, 82, 68, 40, 76, 118, 54]
        })
        fig = px.line(by_day, x="Día", y="Carga", markers=True)
        fig.update_traces(line_color="#bb5cff", marker_color="#ffffff", line_width=4)
        fig.update_layout(
            height=360, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.02)",
            margin=dict(l=10, r=10, t=20, b=10), font=dict(color="#f4efff")
        )
        st.plotly_chart(fig, use_container_width=True)
    with right:
        st.markdown("<div class='glass' style='padding:1.2rem'>", unsafe_allow_html=True)
        st.markdown("#### Próxima sesión")
        st.markdown("### Brick session")
        st.markdown("<p class='small'>45 min bici Z3 + 20 min carrera controlada</p>", unsafe_allow_html=True)
        st.progress(0.65, text="Carga objetivo 65%")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### Estado de bienestar")
        st.markdown("<p class='small'>Sueño: 7.8 h · Fatiga: media · Dolor muscular: bajo</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    b1, b2 = st.columns(2, gap="large")
    with b1:
        sports = df.groupby("Disciplina", as_index=False)["Duración (min)"].sum()
        fig2 = px.bar(sports, x="Disciplina", y="Duración (min)", color="Disciplina", color_discrete_sequence=["#bb5cff", "#7f8cff", "#39d98a", "#ffb547"])
        fig2.update_layout(height=320, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.02)", margin=dict(l=10,r=10,t=10,b=10), font=dict(color="#f4efff"), showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)
    with b2:
        st.markdown("<div class='glass' style='padding:1.2rem'>", unsafe_allow_html=True)
        st.markdown("#### Objetivos de la semana")
        st.markdown("- Completar 2 sesiones de natación\n- Mantener fondo largo en bicicleta\n- Ejecutar brick del fin de semana\n- Registrar RPE y bienestar diario")
        st.markdown("</div>", unsafe_allow_html=True)
