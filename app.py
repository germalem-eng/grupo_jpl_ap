import streamlit as st
import time
import pandas as pd
import numpy as np

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="App JPL", layout="wide", initial_sidebar_state="expanded")

# --- 2. ESTILOS CSS (Personalización Institucional) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }

    /* Sidebar Vinotinto */
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Fondo con Marca de Agua */
    .stApp {
        background-color: #F2F2F2;
        background-image: url("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg");
        background-repeat: no-repeat; background-attachment: fixed; background-position: center; background-size: 40%;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(242, 242, 242, 0.94); z-index: -1;
    }

    .top-bar { background-color: #800000; padding: 20px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin-top: -60px; }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #F2F2F2; color: #555; text-align: center; padding: 5px; font-size: 11px; border-top: 1px solid #800000; z-index: 100; }
    .alerta-roja { padding: 15px; background-color: #ffcccc; border-left: 6px solid #ff0000; border-radius: 8px; color: #900; }
    .alerta-verde { padding: 15px; background-color: #d4edda; border-left: 6px solid #28a745; border-radius: 8px; color: #155724; }
</style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE SESIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'
if 'autenticado' not in st.session_state: st.session_state.autenticado = False
CODIGO_VIDEO_OK = "JPL2026" # Código válido por 15 días corridos

# --- 4. BARRA LATERAL (ACCESO) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    st.markdown("### ACCESO")
    if not st.session_state.autenticado:
        u = st.text_input("Usuario")
        p = st.text_input("Clave", type="password")
        if st.button("INGRESAR"):
            if u == "Gerardo" and p == "1234":
                st.session_state.autenticado = True
                st.rerun()
    else:
        st.success("Sesión Activa")
        if st.button("CERRAR SESIÓN"):
            st.session_state.autenticado = False
            st.rerun()
    
    st.divider()
    if st.button("🏠 INICIO EVALUACIÓN"): st.session_state.pantalla = 'inicio'; st.rerun()
    if st.button("📊 ESTADÍSTICAS"): st.session_state.pantalla = 'stats'; st.rerun()
    if st.button("🎥 VIDEOTECA"): st.session_state.pantalla = 'videos'; st.rerun()

# --- 5. CUERPO DE LA APP ---

if st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar"><h1>App JPL</h1><p>Gestión de Estándares Mínimos Res. 0312</p></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏢 Micro (<10 trabajadores)\n7 Estándares"): st.session_state.nivel = "7"; st.session_state.pantalla = 'lista'
    with col2:
        if st.button("🏬 Pyme (11-50 trabajadores)\n21 Estándares"): st.session_state.nivel = "21"; st.session_state.pantalla = 'lista'
    with col3:
        if st.button("🏭 Grande (>50 o Riesgo IV-V)\n62 Estándares"): st.session_state.nivel = "62"; st.session_state.pantalla = 'lista'

elif st.session_state.pantalla == 'lista':
    st.markdown(f'<div class="top-bar"><h2>Nivel: {st.session_state.nivel} Estándares</h2></div>', unsafe_allow_html=True)
    
    # Simulación de carga de items según la resolución
    items_list = {
        "7": ["Asignación de responsable del SG-SST", "Afiliación al Sistema de Seguridad Social", "Plan Anual de Trabajo"],
        "21": ["Asignación de recursos", "Capacitación en SST", "Evaluaciones Médicas Ocupacionales"],
        "62": ["Política de SST", "Objetivos del SG-SST", "Matriz de Requisitos Legales"]
    }

    for i in items_list.get(st.session_state.nivel, []):
        st.checkbox(f"Estándar: {i}", disabled=not st.session_state.autenticado)

    if not st.session_state.autenticado:
        st.warning("⚠️ MODO LECTURA: Para interactuar, debe ser Cliente Asociado.")
    
    if st.button("Volver al Inicio"): st.session_state.pantalla = 'inicio'; st.rerun()

elif st.session_state.pantalla == 'stats':
    st.markdown('<div class="top-bar"><h2>Panel de Estadísticas y Alertas</h2></div>', unsafe_allow_html=True)
    
    # Alertas Tempranas
    st.subheader("⚠️ Sistema de Alerta Temprana (Res. 0312)")
    col_a, col_b = st.columns(2)
    with col_a:
        acc = st.number_input("Indice de Accidentalidad Mensual", min_value=0.0, value=2.0)
    with col_b:
        aus = st.number_input("Días de Ausentismo", min_value=0, value=5)

    if acc > 5.0 or aus > 10:
        st.markdown('<div class="alerta-roja">🚨 **ALERTA TEMPRANA:** Los indicadores superan el umbral preventivo. Riesgo de incumplimiento ante MinTrabajo.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="alerta-verde">✅ **CUMPLIMIENTO:** Sus indicadores se mantienen en niveles seguros.</div>', unsafe_allow_html=True)

    # Gráficos
    st.divider()
    if st.session_state.autenticado:
        st.write("### Gráficos de Gestión para Clientes Premium")
        df = pd.DataFrame({"Categoría": ["Cumple", "No Cumple", "En Proceso"], "Valor": [60, 15, 25]})
        st.bar_chart(df, x="Categoría", y="Valor")
        st.download_button("📥 Descargar Reporte Estadístico (PDF)", data="PDF_DATA", file_name="Reporte_JPL.pdf")
    else:
        st.info("Gráficos avanzados disponibles solo para Asociados.")

elif st.session_state.pantalla == 'videos':
    st.markdown('<div class="top-bar"><h2>Videoteca Técnica JPL</h2></div>', unsafe_allow_html=True)
    
    code = st.text_input("Ingrese código de acceso (Validez 15 días corridos):", type="password")
    if code == CODIGO_VIDEO_OK:
        st.success("Acceso concedido (Incluye sábados, domingos y festivos).")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.button("📥 Descargar Video")
    else:
        st.error("Código inválido o vencido.")

# --- 6. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
