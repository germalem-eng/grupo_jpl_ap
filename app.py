import streamlit as st
import time
import pandas as pd

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="App JPL", layout="wide")

# --- 2. ESTILOS CSS (Vinotinto Institucional) ---
st.markdown("""
<style>
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stApp { background-color: #F2F2F2; }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; text-align: center; padding: 10px; font-size: 12px; border-top: 1px solid #800000; background: white; z-index: 100; }
    .alerta-roja { padding: 10px; background-color: #ffcccc; border-left: 5px solid red; border-radius: 5px; margin: 10px 0; }
    .alerta-verde { padding: 10px; background-color: #d4edda; border-left: 5px solid green; border-radius: 5px; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE NAVEGACIÓN ---
if 'autenticado' not in st.session_state: st.session_state.autenticado = False
if 'seccion' not in st.session_state: st.session_state.seccion = None

# --- 4. BARRA LATERAL (ACCESO) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    st.header("ACCESO")
    if not st.session_state.autenticado:
        user = st.text_input("Usuario")
        pw = st.text_input("Clave", type="password")
        if st.button("Ingresar"):
            if user == "Gerardo" and pw == "1234":
                st.session_state.autenticado = True
                st.rerun()
    else:
        st.success("Conectado")
        if st.button("Cerrar Sesión"):
            st.session_state.autenticado = False
            st.rerun()
    
    st.divider()
    if st.button("🏠 Inicio"): st.session_state.seccion = None

# --- 5. CUERPO PRINCIPAL ---
st.title("App JPL - Gestión SST")

if st.session_state.seccion is None:
    st.subheader("Seleccione el nivel de la empresa:")
    col1, col2, col3 = st.columns(3)
    
    # Botones con asignación de estado para que no se pierda el click
    if col1.button("🏢 Micro (7 ítems)"): st.session_state.seccion = "7"
    if col2.button("🏬 Pyme (21 ítems)"): st.session_state.seccion = "21"
    if col3.button("🏭 Grande (62 ítems)"): st.session_state.seccion = "62"

# --- DESPLIEGUE DE ÍTEMS Y ALERTAS ---
if st.session_state.seccion:
    st.info(f"Evaluando Estándares Mínimos: Nivel {st.session_state.seccion}")
    
    tab1, tab2 = st.tabs(["📋 Auditoría", "⚠️ Alertas e Indicadores"])
    
    with tab1:
        # Diccionario de ítems según resolución 0312
        items = {
            "7": ["1.1.1 Responsable del SG-SST", "1.1.3 Asignación de recursos", "6.1.1 Identificación de peligros"],
            "21": ["1.1.1 Responsable", "1.2.1 Programa Capacitación", "2.1.1 Evaluación Inicial", "4.2.1 Identificación de Peligros"],
            "62": ["1.1.1 Responsable", "1.1.8 Reconocimiento de SST", "3.1.1 Evaluaciones Médicas", "etc..."]
        }
        
        for it in items.get(st.session_state.seccion, []):
            st.checkbox(it, disabled=not st.session_state.autenticado)

    with tab2:
        st.subheader("Indicadores y Alertas Tempranas")
        # Lógica de alerta temprana basada en Res. 0312
        accidentalidad = st.number_input("Tasa de accidentalidad actual (%)", min_value=0.0)
        
        if accidentalidad > 5.0:
            st.markdown('<div class="alerta-roja">🚨 **ALERTA CRÍTICA:** Su tasa de accidentalidad supera el límite permitido. Se requiere intervención inmediata en el Plan de Trabajo.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="alerta-verde">✅ **ESTADO ÓPTIMO:** Los indicadores están dentro del rango de cumplimiento preventivo.</div>', unsafe_allow_html=True)

    if st.button("Volver al Menú"):
        st.session_state.seccion = None
        st.rerun()

# --- 6. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
