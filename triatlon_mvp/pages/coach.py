import streamlit as st
import pandas as pd


def render_coach():
    st.markdown("<div class='section-title'>Panel del coach</div>", unsafe_allow_html=True)
    athletes = st.session_state.athletes
    st.dataframe(athletes, use_container_width=True, hide_index=True)

    st.markdown("### Asignación rápida")
    c1, c2, c3 = st.columns(3)
    atleta = c1.selectbox("Atleta", athletes["Atleta"].tolist())
    plan = c2.text_input("Plan", placeholder="Plan olímpico build")
    nota = c3.text_input("Nota", placeholder="Ajustar carga por fatiga")
    if st.button("Guardar ajuste"):
        st.success(f"Ajuste guardado para {atleta}: {plan or 'plan actualizado'}")

    st.markdown("<div class='glass' style='padding:1.2rem'>", unsafe_allow_html=True)
    st.markdown("#### Alertas del día")
    st.markdown("- Ana Torres presenta fatiga alta y cumplimiento 76%\n- María Cristina no ha registrado wellness hoy\n- Carlos Vega listo para aumentar volumen el fin de semana")
    st.markdown("</div>", unsafe_allow_html=True)
