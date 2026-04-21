import streamlit as st


def render_membership():
    st.markdown("<div class='section-title'>Membresía y monetización</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    plans = [
        ("Starter", "$19 USD/mes", ["1 atleta", "Plan semanal", "Registro de actividades"]),
        ("Performance", "$49 USD/mes", ["Hasta 15 atletas", "Panel coach", "Métricas avanzadas"]),
        ("Elite Studio", "$99 USD/mes", ["Atletas ilimitados", "Operación multi-coach", "Analítica premium"]),
    ]
    for col, (title, price, feats) in zip([c1, c2, c3], plans):
        with col:
            st.markdown("<div class='glass' style='padding:1.25rem; min-height:280px'>", unsafe_allow_html=True)
            st.markdown(f"### {title}")
            st.markdown(f"## {price}")
            st.markdown("\n".join([f"- {x}" for x in feats]))
            st.button(f"Elegir {title}", key=title, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    st.info("En producción este módulo se integraría con Stripe Billing para suscripciones recurrentes y gestión de cobros.")
