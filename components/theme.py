import streamlit as st


def inject_theme():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        :root {
            --bg: #0a0614;
            --bg2: #120a24;
            --card: rgba(20, 14, 36, 0.78);
            --card-2: rgba(34, 21, 57, 0.82);
            --line: rgba(255,255,255,0.08);
            --txt: #f4efff;
            --muted: #b8abdb;
            --accent: #bb5cff;
            --accent-2: #6f7cff;
            --good: #39d98a;
            --warn: #ffb547;
        }
        html, body, [class*="css"]  {font-family: 'Inter', sans-serif;}
        .stApp {
            background:
                radial-gradient(circle at 15% 10%, rgba(187,92,255,0.22), transparent 26%),
                radial-gradient(circle at 85% 12%, rgba(111,124,255,0.20), transparent 24%),
                linear-gradient(180deg, #160d29 0%, #090511 100%);
            color: var(--txt);
        }
        [data-testid="stSidebar"] {
            background: rgba(12, 8, 22, 0.95);
            border-right: 1px solid var(--line);
        }
        [data-testid="stSidebarNav"] * {color: var(--txt) !important;}
        .block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
        .hero-card, .login-card, .glass, div[data-testid="stMetric"] {
            background: linear-gradient(180deg, rgba(30,20,50,.82), rgba(12,9,24,.82));
            border: 1px solid rgba(255,255,255,.08);
            box-shadow: 0 10px 35px rgba(0,0,0,.28), inset 0 1px 0 rgba(255,255,255,.04);
            border-radius: 24px;
            backdrop-filter: blur(18px);
        }
        .hero-card {padding: 2rem; min-height: 420px; display:flex; flex-direction:column; justify-content:center;}
        .login-card {padding: 1.5rem; margin-top: 1rem;}
        .eyebrow {font-size: .82rem; color: #d8c4ff; letter-spacing: .18em; font-weight: 700; margin-bottom: .8rem;}
        .hero-title {font-size: clamp(2rem, 4vw, 4.2rem); line-height: 1.02; margin: 0 0 1rem 0;}
        .hero-text {font-size: 1.05rem; color: var(--muted); max-width: 52ch;}
        .hero-chips {display:flex; flex-wrap:wrap; gap:.65rem; margin-top:1.25rem;}
        .hero-chips span, .pill {
            background: rgba(187,92,255,.14); color:#efd7ff; border:1px solid rgba(187,92,255,.28);
            padding:.48rem .85rem; border-radius:999px; font-size:.84rem;
        }
        .topbar {
            display:flex; justify-content:space-between; align-items:center; gap:1rem;
            padding:1rem 1.1rem; margin-bottom:1rem;
            background: rgba(18,10,36,.75); border:1px solid var(--line); border-radius:22px;
        }
        .topbar h2 {margin:0; font-size:1.15rem;}
        .muted {color: var(--muted);}
        .section-title {font-size:1.15rem; font-weight:700; margin: .4rem 0 1rem 0;}
        div[data-testid="stMetric"] {padding: 1rem;}
        div[data-testid="stMetric"] label {color: var(--muted) !important;}
        .stButton>button, .stDownloadButton>button {
            border-radius: 14px; border: 1px solid rgba(255,255,255,.08);
            background: linear-gradient(90deg, var(--accent), #8d5cff);
            color: white; font-weight: 700;
        }
        .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div,
        .stMultiSelect div[data-baseweb="select"] > div, .stNumberInput input, .stDateInput input {
            background: rgba(255,255,255,.04) !important; color: var(--txt) !important;
            border: 1px solid rgba(255,255,255,.08) !important; border-radius: 14px !important;
        }
        .stTabs [data-baseweb="tab-list"] {gap: .45rem;}
        .stTabs [data-baseweb="tab"] {
            background: rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.06);
            border-radius: 12px; padding: .55rem .95rem; color: var(--txt);
        }
        .stTabs [aria-selected="true"] {background: rgba(187,92,255,.18) !important;}
        .plan-card {
            background: linear-gradient(180deg, rgba(88,61,155,.42), rgba(24,14,42,.85));
            border:1px solid rgba(255,255,255,.08); border-radius:20px; padding:1rem; min-height:170px;
        }
        .small {font-size:.84rem; color: var(--muted);}
        </style>
        """,
        unsafe_allow_html=True,
    )


def topbar():
    role = st.session_state.get("role", "Atleta")
    athlete = st.session_state.get("athlete_name", "Atleta")
    st.markdown(
        f"""
        <div class='topbar'>
            <div>
                <div class='eyebrow' style='margin-bottom:.35rem'>TRICOACH PRO</div>
                <h2>{athlete} · {role}</h2>
                <div class='muted'>MVP de entrenamiento personalizado y seguimiento integral</div>
            </div>
            <div class='pill'>Global · Mobile first · Demo SaaS</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.sidebar:
        st.markdown(f"### {athlete}")
        st.caption(f"Perfil activo: {role}")
        if st.button("Cerrar sesión", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
