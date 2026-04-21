import streamlit as st
from pages.dashboard import render_dashboard
from pages.plan import render_plan
from pages.activities import render_activities
from pages.coach import render_coach
from pages.membership import render_membership
from components.theme import inject_theme, topbar
from data.demo_data import init_demo_state

st.set_page_config(
    page_title="TriCoach Pro",
    page_icon="🏊",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_theme()
init_demo_state()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "role" not in st.session_state:
    st.session_state.role = "Atleta"
if "athlete_name" not in st.session_state:
    st.session_state.athlete_name = "María Cristina"

if not st.session_state.logged_in:
    c1, c2 = st.columns([1.1, 0.9], gap="large")
    with c1:
        st.markdown("<div class='hero-card'>", unsafe_allow_html=True)
        st.markdown("<div class='eyebrow'>TRICOACH PRO</div>", unsafe_allow_html=True)
        st.markdown("<h1 class='hero-title'>Entrena triatlón con una experiencia premium y seguimiento real.</h1>", unsafe_allow_html=True)
        st.markdown("<p class='hero-text'>MVP funcional en Streamlit con planificación, carga de actividades, panel para coach, métricas y monetización por membresía.</p>", unsafe_allow_html=True)
        st.markdown("<div class='hero-chips'><span>Natación</span><span>Ciclismo</span><span>Carrera</span><span>Fuerza</span></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        st.markdown("### Ingreso a la plataforma")
        email = st.text_input("Correo", placeholder="coach@tricoachpro.com")
        password = st.text_input("Contraseña", type="password", placeholder="••••••••")
        role = st.selectbox("Perfil", ["Atleta", "Coach"])
        athlete_name = st.text_input("Nombre visible", value=st.session_state.athlete_name)
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
