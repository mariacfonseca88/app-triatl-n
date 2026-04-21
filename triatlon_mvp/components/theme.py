import streamlit as st

HERO_BIKE = "https://pplx-res.cloudinary.com/image/upload/pplx_search_images/41f6ff258429f5fe531d5176a6e52eec62669d79.jpg"
HERO_SWIM = "https://pplx-res.cloudinary.com/image/upload/pplx_search_images/2ab52f876b5784416f452f02afb6c83aed87bfa1.jpg"
HERO_RUN = "https://pplx-res.cloudinary.com/image/upload/pplx_search_images/3561510b2800f2cf8690beba61841294a0fdb57c.jpg"


def inject_theme():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        :root {{
            --bg: #090511;
            --bg2: #140b27;
            --card: rgba(20, 14, 36, 0.76);
            --card-2: rgba(34, 21, 57, 0.84);
            --line: rgba(255,255,255,0.09);
            --txt: #f4efff;
            --muted: #b8abdb;
            --accent: #bb5cff;
            --accent-2: #6f7cff;
            --good: #39d98a;
            --warn: #ffb547;
        }}
        html, body, [class*="css"] {{font-family: 'Inter', sans-serif;}}
        .stApp {{
            background:
                radial-gradient(circle at 12% 8%, rgba(187,92,255,0.22), transparent 24%),
                radial-gradient(circle at 86% 10%, rgba(111,124,255,0.16), transparent 20%),
                linear-gradient(180deg, #160d29 0%, #090511 100%);
            color: var(--txt);
        }}
        [data-testid="stHeader"] {{background: rgba(0,0,0,0);}}
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, rgba(9,5,17,.98), rgba(14,8,28,.96));
            border-right: 1px solid var(--line);
        }}
        [data-testid="stSidebarNav"] * {{color: var(--txt) !important;}}
        .block-container {{padding-top: 1rem; padding-bottom: 2rem; max-width: 1450px;}}
        .hero-card, .login-card, .glass, div[data-testid="stMetric"] {{
            background: linear-gradient(180deg, rgba(30,20,50,.76), rgba(12,9,24,.84));
            border: 1px solid rgba(255,255,255,.08);
            box-shadow: 0 10px 35px rgba(0,0,0,.28), inset 0 1px 0 rgba(255,255,255,.04);
            border-radius: 26px;
            backdrop-filter: blur(18px);
        }}
        .hero-card {{padding: 0; min-height: 560px; overflow:hidden; position:relative;}}
        .hero-visual {{
            position:relative; min-height:560px; border-radius:26px; overflow:hidden;
            background:
                linear-gradient(180deg, rgba(8,6,18,.18), rgba(7,4,15,.68)),
                linear-gradient(120deg, rgba(187,92,255,.24), rgba(7,4,15,.12)),
                url('{HERO_BIKE}');
            background-size:cover; background-position:center;
        }}
        .hero-overlay {{
            position:absolute; inset:0;
            background: linear-gradient(180deg, rgba(10,7,18,.08) 0%, rgba(10,7,18,.78) 70%, rgba(9,5,17,.95) 100%);
        }}
        .hero-copy {{position:absolute; left:2.2rem; right:2.2rem; bottom:2rem; z-index:2;}}
        .eyebrow {{font-size: .82rem; color: #e2d3ff; letter-spacing: .18em; font-weight: 700; margin-bottom: .8rem;}}
        .hero-title {{font-size: clamp(2.3rem, 4vw, 4.5rem); line-height: 1.02; margin: 0 0 1rem 0; max-width: 9ch;}}
        .hero-text {{font-size: 1rem; color: #e2daf9; max-width: 50ch;}}
        .hero-chips {{display:flex; flex-wrap:wrap; gap:.65rem; margin-top:1.25rem;}}
        .hero-chips span, .pill {{
            background: rgba(187,92,255,.16); color:#f2dcff; border:1px solid rgba(187,92,255,.28);
            padding:.48rem .85rem; border-radius:999px; font-size:.84rem;
        }}
        .floating-kpi {{
            position:absolute; top:1.4rem; right:1.4rem; z-index:2; width:220px;
            background: rgba(15,10,27,.55); border:1px solid rgba(255,255,255,.08);
            border-radius:22px; padding:1rem; backdrop-filter: blur(18px);
        }}
        .kpi-grid {{display:grid; grid-template-columns:1fr 1fr; gap:.75rem; margin-top:.9rem;}}
        .kpi-box {{background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.06); padding:.8rem; border-radius:16px;}}
        .login-card {{padding: 1.6rem; margin-top: .4rem; min-height:560px; display:flex; flex-direction:column; justify-content:center;}}
        .topbar {{
            display:flex; justify-content:space-between; align-items:center; gap:1rem;
            padding:1rem 1.1rem; margin-bottom:1rem;
            background: rgba(18,10,36,.75); border:1px solid var(--line); border-radius:22px;
        }}
        .topbar h2 {{margin:0; font-size:1.15rem;}}
        .muted {{color: var(--muted);}}
        .section-title {{font-size:1.15rem; font-weight:700; margin: .3rem 0 1rem 0;}}
        div[data-testid="stMetric"] {{padding: 1rem;}}
        div[data-testid="stMetric"] label {{color: var(--muted) !important;}}
        .stButton>button, .stDownloadButton>button {{
            border-radius: 14px; border: 1px solid rgba(255,255,255,.08);
            background: linear-gradient(90deg, var(--accent), #8d5cff);
            color: white; font-weight: 700;
        }}
        .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div,
        .stMultiSelect div[data-baseweb="select"] > div, .stNumberInput input, .stDateInput input {{
            background: rgba(255,255,255,.045) !important; color: var(--txt) !important;
            border: 1px solid rgba(255,255,255,.08) !important; border-radius: 14px !important;
        }}
        .stTabs [data-baseweb="tab-list"] {{gap: .45rem;}}
        .stTabs [data-baseweb="tab"] {{
            background: rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.06);
            border-radius: 12px; padding: .55rem .95rem; color: var(--txt);
        }}
        .stTabs [aria-selected="true"] {{background: rgba(187,92,255,.18) !important;}}
        .plan-card {{
            background: linear-gradient(180deg, rgba(88,61,155,.42), rgba(24,14,42,.85));
            border:1px solid rgba(255,255,255,.08); border-radius:20px; padding:1rem; min-height:190px;
        }}
        .banner-card {{
            position:relative; min-height:260px; overflow:hidden; border-radius:24px;
            background:
                linear-gradient(120deg, rgba(12,10,21,.38), rgba(9,5,17,.82)),
                url('{HERO_RUN}');
            background-size:cover; background-position:center;
            border:1px solid rgba(255,255,255,.08);
            box-shadow: 0 10px 35px rgba(0,0,0,.28);
            margin-bottom:1rem;
        }}
        .banner-card.swim {{
            background:
                linear-gradient(120deg, rgba(12,10,21,.34), rgba(9,5,17,.8)),
                url('{HERO_SWIM}');
            background-size:cover; background-position:center;
        }}
        .banner-copy {{position:absolute; left:1.6rem; bottom:1.4rem; right:1.6rem;}}
        .small {{font-size:.84rem; color: var(--muted);}}
        .mini-stat-row {{display:flex; gap:.8rem; flex-wrap:wrap; margin-top:1rem;}}
        .mini-stat {{background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.07); border-radius:16px; padding:.75rem .9rem; min-width:120px;}}
        @media (max-width: 980px) {{
            .hero-card, .hero-visual, .login-card {{min-height: 420px;}}
            .hero-copy {{left:1.25rem; right:1.25rem; bottom:1.25rem;}}
            .floating-kpi {{position:absolute; width:180px; top:1rem; right:1rem;}}
        }}
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
                <div class='muted'>Seguimiento premium de triatlón con visión global de rendimiento</div>
            </div>
            <div class='pill'>Swim · Bike · Run</div>
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
