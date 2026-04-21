import streamlit as st
import pandas as pd


def render_plan():
    st.markdown("<div class='section-title'>Plan personalizado</div>", unsafe_allow_html=True)
    plan = st.session_state.plan
    cols = st.columns(len(plan))
    for i, (_, row) in enumerate(plan.iterrows()):
        with cols[i]:
            st.markdown(f"""
            <div class='plan-card'>
                <div class='small'>{row['Día']}</div>
                <h4 style='margin:.4rem 0'>{row['Disciplina']}</h4>
                <div class='small'>{row['Objetivo']}</div>
                <div style='margin-top:1rem' class='pill'>Carga {row['Carga']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### Cargue de programa")
    c1, c2 = st.columns([1,1])
    with c1:
        nombre = st.text_input("Nombre del bloque", placeholder="Base 70.3 · Semana 4")
        disciplina = st.selectbox("Disciplina", ["Natación", "Ciclismo", "Carrera", "Fuerza", "Recuperación"])
        objetivo = st.text_area("Objetivo", placeholder="Describe la sesión o bloque")
    with c2:
        dia = st.selectbox("Día", ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"])
        carga = st.slider("Carga estimada", 10, 180, 60)
        estado = st.selectbox("Estado", ["Programado", "Ajustado", "Completado"])

    if st.button("Agregar sesión al plan"):
        if nombre or objetivo:
            new_row = pd.DataFrame([{
                "Día": dia, "Disciplina": disciplina, "Objetivo": objetivo or nombre, "Carga": carga, "Estado": estado
            }])
            st.session_state.plan = pd.concat([st.session_state.plan, new_row], ignore_index=True)
            st.success("Sesión agregada al plan del atleta")
            st.rerun()
