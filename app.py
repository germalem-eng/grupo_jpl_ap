import streamlit as st
import time
import pandas as pd
import numpy as np

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="L.I.N.A. | Grupo JPL", layout="wide", initial_sidebar_state="expanded")

# --- 2. ESTILOS CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }

    /* Sidebar Vinotinto */
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Fondo Principal con Marca de Agua */
    .stApp {
        background-color: #F2F2F2;
        background-image: url("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg");
        background-repeat: no-repeat; background-attachment: fixed; background-position: center; background-size: 45%;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(242, 242, 242, 0.94); z-index: -1;
    }

    .top-bar { background-color: #800000; padding: 20px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin-top: -60px; }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #F2F2F2; color: #555; text-align: center; padding: 5px; font-size: 12px; border-top: 1px solid #800000; z-index: 100; }
</style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE SESIÓN Y SEGURIDAD ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'
if 'autenticado' not in st.session_state: st.session_state.autenticado = False

# Simulación de código de video (válido 15 días)
CODIGO_VIDEO_OK = "JPL2026" 

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    st.markdown("## ACCESO L.I.N.A.")
    
    if not st.session_state.autenticado:
        user = st.text_input("Usuario")
        pw = st.text_input("Clave", type="password")
        if st.button("INGRESAR"):
            if user == "Gerardo" and pw == "1234": # Ejemplo
                st.session_state.autenticado = True
                st.rerun()
    else:
        st.success("Sesión Iniciada")
        if st.button("CERRAR SESIÓN"):
            st.session_state.autenticado = False
            st.rerun()
    
    st.divider()
    if st.button("🏠 INICIO"): st.session_state.pantalla = 'inicio'; st.rerun()
    if st.button("📊 ESTADÍSTICAS"): st.session_state.pantalla = 'graficos'; st.rerun()
    if st.button("🎥 VIDEOTECA"): st.session_state.pantalla = 'videos'; st.rerun()

# --- 5. PANTALLAS ---

# --- PANTALLA: INICIO ---
if st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar"><h1>L.I.N.A.</h1><p>Logística • Inteligencia • Nuevos • Algoritmos</p></div>', unsafe_allow_html=True)
    st.write("### 📂 Evaluación Estándares Mínimos")
    
    c1, c2, c3 = st.columns(3)
    with c1: st.button("🏢 Micro (<10)")
    with c2: st.button("🏬 Pyme (11-50)")
    with c3: st.button("🏭 Grande (>50 / R IV-V)")
    
    if not st.session_state.autenticado:
        st.info("⚠️ Modo Lectura: Inicie sesión para interactuar.")

# --- PANTALLA: GRÁFICOS (Estadísticas descargables) ---
elif st.session_state.pantalla == 'graficos':
    st.markdown('<div class="top-bar"><h2>PANEL DE ESTADÍSTICAS JPL</h2></div>', unsafe_allow_html=True)
    
    if st.session_state.autenticado:
        col_g1, col_g2 = st.columns(2)
        
        with col_g1:
            st.write("#### Cumplimiento General")
            data = pd.DataFrame({"Estado": ["Cumple", "No Cumple"], "Valor": [75, 25]})
            st.pie_chart(data, x="Estado", y="Valor")
            
        with col_g2:
            st.write("#### Histórico de Hallazgos")
            chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Mes Ant', 'Mes Act'])
            st.line_chart(chart_data)
            
        st.download_button("📥 Descargar Reporte Estadístico (PDF/Excel)", data="...", file_name="reporte_jpl.txt")
    else:
        st.warning("Acceso exclusivo para asociados actuales o Premium.")

# --- PANTALLA: VIDEOS (Con código de verificación) ---
elif st.session_state.pantalla == 'videos':
    st.markdown('<div class="top-bar"><h2>REPOSITORIO TÉCNICO JPL</h2></div>', unsafe_allow_html=True)
    
    check_code = st.text_input("Ingrese código de acceso (Válido por 15 días calendario):", type="password")
    
    if check_code == CODIGO_VIDEO_OK:
        st.success("Acceso concedido.")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Ejemplo de video
        st.write("📂 **Material de descarga:** [Guía_SST_JPL.pdf]")
    else:
        st.error("Código incorrecto o vencido (Incluye fines de semana y festivos).")

# --- 6. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | L.I.N.A. V2.0 | Desarrollado por Ing. Gerardo Martinez | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
