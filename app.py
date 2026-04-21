import streamlit as st
from pages.dashboard import render_dashboard
from pages.plan import render_plan
from pages.activities import render_activities
from pages.coach import render_coach
from pages.membership import render_membership
from components.theme import inject_theme, topbar
from data.demo_data import init_demo_state

st.set_page_config(page_title="Coach Camilo Fonseca - Smart Swimming", page_icon="🏊", layout="wide", initial_sidebar_state="expanded")

inject_theme()
init_demo_state()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = "Atleta"
if "athlete_name" not in st.session_state:
    st.session_state.athlete_name = "María Cristina"

if not st.session_state.logged_in:
    c1, c2 = st.columns([1.15, 0.85], gap="large")
    with c1:
        st.markdown("""
        <div class='hero-card'>
            <div class='hero-visual'>
                <div class='hero-overlay'></div>
                <div class='floating-kpi'>
                    <div class='small'>Estado del nadador</div>
                    <h3 style='margin:.35rem 0 0 0'>Smart Swimming</h3>
                    <div class='kpi-grid'>
                        <div class='kpi-box'><div class='small'>Técnica</div><div style='font-size:1.3rem;font-weight:800'>91%</div></div>
                        <div class='kpi-box'><div class='small'>Carga</div><div style='font-size:1.3rem;font-weight:800'>74</div></div>
                        <div class='kpi-box'><div class='small'>RPE</div><div style='font-size:1.3rem;font-weight:800'>6.4</div></div>
                        <div class='kpi-box'><div class='small'>Sueño</div><div style='font-size:1.3rem;font-weight:800'>7.8h</div></div>
                    </div>
                </div>
                <div class='hero-copy'>
                    <div class='eyebrow'>COACH CAMILO FONSECA</div>
                    <h1 class='hero-title'>Smart Swimming con imagen más pro y enfoque premium</h1>
                    <p class='hero-text'>Planificación, adherencia, bienestar y progreso técnico del nadador en una sola plataforma visualmente superior.</p>
                    <div class='hero-chips'><span>Natación</span><span>Técnica</span><span>Wellness</span><span>Seguimiento</span></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        st.markdown("### Ingreso a la plataforma")
        st.markdown("<p class='small'>Experiencia visual refinada para coach y atleta.</p>", unsafe_allow_html=True)
        st.text_input("Correo", placeholder="coach@smartswimming.com")
        st.text_input("Contraseña", type="password", placeholder="••••••••")
        role = st.selectbox("Perfil", ["Atleta", "Coach"])
        athlete_name = st.text_input("Nombre visible", value=st.session_state.athlete_name)
        st.markdown("<div class='mini-stat-row'><div class='mini-stat'><div class='small'>Sesiones</div><div style='font-weight:800;font-size:1.2rem'>148</div></div><div class='mini-stat'><div class='small'>Adherencia</div><div style='font-weight:800;font-size:1.2rem'>89%</div></div><div class='mini-stat'><div class='small'>Técnica</div><div style='font-weight:800;font-size:1.2rem'>91%</div></div></div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Entrar al MVP", use_container_width=True, type="primary"):
            st.session_state.logged_in = True
            st.session_state.role = role
            st.session_state.athlete_name = athlete_name or "Atleta"
            st.rerun()
        st.caption("Demo funcional orientada a validación comercial, no autenticación productiva.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

pages = {
    "Inicio": st.Page(render_dashboard, title="Dashboard", icon="🏠"),
    "Plan": st.Page(render_plan, title="Plan", icon="🗓️"),
    "Actividades": st.Page(render_activities, title="Actividades", icon="📈"),
    "Coach": st.Page(render_coach, title="Coach", icon="🎯"),
    "Membresía": st.Page(render_membership, title="Membresía", icon="💳"),
}

if st.session_state.role == "Atleta":
    nav = st.navigation({"App": [pages["Inicio"], pages["Plan"], pages["Actividades"], pages["Membresía"]]})
else:
    nav = st.navigation({"App": [pages["Inicio"], pages["Plan"], pages["Actividades"], pages["Coach"], pages["Membresía"]]})

topbar()
nav.run()
