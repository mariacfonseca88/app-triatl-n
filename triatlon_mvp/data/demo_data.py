import streamlit as st
import pandas as pd
from datetime import date, timedelta


def init_demo_state():
    if "activities" not in st.session_state:
        st.session_state.activities = pd.DataFrame([
            {"Fecha": date.today() - timedelta(days=5), "Disciplina": "Natación", "Sesión": "Técnica + series", "Duración (min)": 55, "Distancia": 2.4, "RPE": 6, "Estado": "Completado"},
            {"Fecha": date.today() - timedelta(days=4), "Disciplina": "Ciclismo", "Sesión": "Rodaje Z2", "Duración (min)": 110, "Distancia": 52.3, "RPE": 5, "Estado": "Completado"},
            {"Fecha": date.today() - timedelta(days=3), "Disciplina": "Carrera", "Sesión": "Tempo", "Duración (min)": 48, "Distancia": 9.8, "RPE": 7, "Estado": "Completado"},
            {"Fecha": date.today() - timedelta(days=2), "Disciplina": "Fuerza", "Sesión": "Core + tren inferior", "Duración (min)": 40, "Distancia": 0.0, "RPE": 6, "Estado": "Completado"},
            {"Fecha": date.today() - timedelta(days=1), "Disciplina": "Ciclismo", "Sesión": "Intervalos FTP", "Duración (min)": 75, "Distancia": 31.2, "RPE": 8, "Estado": "Completado"},
        ])
    if "plan" not in st.session_state:
        start = date.today()
        st.session_state.plan = pd.DataFrame([
            {"Día": "Lun", "Disciplina": "Natación", "Objetivo": "Técnica y respiración bilateral", "Carga": 55, "Estado": "Programado"},
            {"Día": "Mar", "Disciplina": "Ciclismo", "Objetivo": "Z2 continua 90 min", "Carga": 78, "Estado": "Programado"},
            {"Día": "Mié", "Disciplina": "Carrera", "Objetivo": "Series 6x800", "Carga": 72, "Estado": "Programado"},
            {"Día": "Jue", "Disciplina": "Fuerza", "Objetivo": "Estabilidad + core", "Carga": 38, "Estado": "Programado"},
            {"Día": "Vie", "Disciplina": "Natación", "Objetivo": "Umbral 10x100", "Carga": 62, "Estado": "Programado"},
            {"Día": "Sáb", "Disciplina": "Ciclismo", "Objetivo": "Fondo 3h", "Carga": 120, "Estado": "Programado"},
            {"Día": "Dom", "Disciplina": "Carrera", "Objetivo": "Brick 40 min", "Carga": 46, "Estado": "Programado"},
        ])
    if "athletes" not in st.session_state:
        st.session_state.athletes = pd.DataFrame([
            {"Atleta": "María Cristina", "Plan": "70.3 Base", "Cumplimiento": 88, "Fatiga": "Media", "Próxima sesión": "Tempo run"},
            {"Atleta": "Carlos Vega", "Plan": "Sprint Build", "Cumplimiento": 93, "Fatiga": "Baja", "Próxima sesión": "Swim drills"},
            {"Atleta": "Ana Torres", "Plan": "Olímpico Peak", "Cumplimiento": 76, "Fatiga": "Alta", "Próxima sesión": "Long ride"},
        ])
