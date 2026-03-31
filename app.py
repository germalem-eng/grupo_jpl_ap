import streamlit as st
import time
import pandas as pd
import numpy as np

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(
    page_title="L.I.N.A. | App JPL", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- 2. BASE DE DATOS DE ACCESO (Asociados/Premium) ---
usuarios_activos = {
    "gerardo@mym.com": "1234",
    "cliente@premium.com": "jpl2026"
}
CODIGO_VIDEO_OK = "JPL2026" # Código para videoteca (Válido 15 días)

# --- 3. INTERFAZ VISUAL PROFESIONAL (Estilos CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }

    /* Barra Lateral Vinotinto Institucional */
    [data-testid="stSidebar"] {
        background-color: #800000;
        color: white;
    }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Fondo con Marca de Agua JPL */
    .stApp {
        background-color: #F2F2F2;
        background-image: url("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg");
        background-repeat: no-repeat; background-attachment: fixed; background-position: center; background-size: 40%;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(242, 242, 242, 0.94); z-index: -1;
    }

    /* Encabezados y Tarjetas */
    .top-bar-jpl { background-color: #800000; padding: 20px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin-top: -60px; }
    .card-proceso { background-color: rgba(255, 255, 255, 0.98); padding: 15px; border-radius: 15px; border-left: 8px solid #800000; margin-bottom: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    
    /* Pie de Página con Créditos */
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #F2F2F2; color: #555; text-align: center; padding: 8px; font-size: 12px; border-top: 1px solid #800000; z-index: 100; }
    
    .stButton>button { background-color: #000000 !important; color: white !important; border-radius: 10px; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 4. CONTROL DE ESTADOS DE SESIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'splash'
if 'autenticado' not in st.session_state: st.session_state.autenticado = False
if 'nivel_sst' not in st.session_state: st.session_state.nivel_sst = "7"

# --- 5. BARRA LATERAL (MENÚ Y LOGIN) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=150)
    st.markdown("## ACCESO L.I.N.A.")
    
    if not st.session_state.autenticado:
        u = st.text_input("Usuario (Correo)")
        p = st.text_input("Clave", type="password")
        if st.button("VALIDAR ACCESO"):
            if u in usuarios_activos and usuarios_activos[u] == p:
                st.session_state.autenticado = True
                st.rerun()
            else: st.error("Credenciales incorrectas")
    else:
        st.success(f"Conectado: {u if 'u' in locals() else 'Asociado'}")
        if st.button("CERRAR SESIÓN"):
            st.session_state.autenticado = False
            st.rerun()
    
    st.divider()
    if st.button("🏠 INICIO / EVALUACIÓN"): st.session_state.pantalla = 'inicio'; st.rerun()
    if st.button("📊 ESTADÍSTICAS JPL"): st.session_state.pantalla = 'graficos'; st.rerun()
    if st.button("🎥 VIDEOTECA TÉCNICA"): st.session_state.pantalla = 'videos'; st.rerun()

# --- 6. LÓGICA DE NAVEGACIÓN ---

# PANTALLA 0: Splash Inicial
if st.session_state.pantalla == 'splash':
    st.markdown('<div style="text-align:center; margin-top:150px;"><h1>App JPL</h1><p>Iniciando proyecto L.I.N.A....</p></div>', unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.pantalla = 'inicio'; st.rerun()

# PANTALLA 1: Inicio y Evaluación SST
elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar-jpl"><h1>L.I.N.A. | App JPL</h1><p>Logística • Inteligencia • Nuevos • Algoritmos</p></div>', unsafe_allow_html=True)
    
    st.write("### 📂 Evaluación Estándares Mínimos (Res. 0312)")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🏢 Micro\n(7 Estándares)"): st.session_state.nivel_sst = "7"; st.session_state.pantalla = 'evaluacion'; st.rerun()
    with c2:
        if st.button("🏬 Pyme\n(21 Estándares)"): st.session_state.nivel_sst = "21"; st.session_state.pantalla = 'evaluacion'; st.rerun()
    with c3:
        if st.button("🏭 Grande / R IV-V\n(62 Estándares)"): st.session_state.nivel_sst = "62"; st.session_state.pantalla = 'evaluacion'; st.rerun()

# PANTALLA 2: Formulario de Evaluación e Indicadores
elif st.session_state.pantalla == 'evaluacion':
    st.markdown(f'<div class="top-bar-jpl"><h3>SST: {st.session_state.nivel_sst} ESTÁNDARES</h3></div>', unsafe_allow_html=True)
    
    t1, t2 = st.tabs(["📋 Auditoría de Ítems", "📈 Indicadores de Gestión"])

    with t1:
        def item_sst(cod, desc):
            st.markdown(f'<div class="card-proceso"><b>{cod}</b>: {desc}</div>', unsafe_allow_html=True)
            return st.selectbox("Estado", ["Pendiente", "Cumple Totalmente", "No Cumple", "No Aplica"], key=cod, disabled=not st.session_state.autenticado)

        if st.session_state.nivel_sst == "7":
            item_sst("1.1.1", "Responsable del Sistema de Gestión de SST")
            item_sst("1.1.3", "Asignación de recursos para el sistema")
            item_sst("6.1.1", "Identificación de peligros y valoración de riesgos")
        # Aquí se pueden expandir los demás casos (21 y 62)

    with t2:
        st.subheader("Reporte de Indicadores Obligatorios")
        colA, colB = st.columns(2)
        with colA:
            st.number_input("Frecuencia de accidentalidad", min_value=0.0, disabled=not st.session_state.autenticado)
            st.number_input("Severidad de accidentalidad", min_value=0.0, disabled=not st.session_state.autenticado)
        with colB:
            st.number_input("Ausentismo por causa médica", min_value=0.0, disabled=not st.session_state.autenticado)
            st.number_input("Proporción de accidentes mortales", min_value=0.0, disabled=not st.session_state.autenticado)

    if not st.session_state.autenticado:
        st.markdown("<br><div style='text-align:center; color:#800000; font-weight:bold;'>⚠️ MODO LECTURA: El acceso para calificar es exclusivo para Asociados o Premium.</div>", unsafe_allow_html=True)

# PANTALLA 3: Panel de Estadísticas (Gráficos)
elif st.session_state.pantalla == 'graficos':
    st.markdown('<div class="top-bar-jpl"><h2>PANEL DE ESTADÍSTICAS JPL</h2></div>', unsafe_allow_html=True)
    
    if st.session_state.autenticado:
        g1, g2 = st.columns(2)
        with g1:
            st.write("#### Porcentaje de Cumplimiento")
            df_pie = pd.DataFrame({"Estado": ["Cumple", "Pendiente"], "Valor": [75, 25]})
            st.pie_chart(df_pie, x="Estado", y="Valor")
        with g2:
            st.write("#### Evolución Mensual")
            df_line = pd.DataFrame(np.random.randn(10, 2), columns=['Meta', 'Logro'])
            st.line_chart(df_line)
        
        st.download_button("📥 DESCARGAR REPORTE PARA CLIENTE", data="Contenido del reporte...", file_name="Reporte_Estadistico_JPL.txt")
    else:
        st.warning("Acceso restringido. Solicite su código de asociado a JPL Prevencionistas SAS.")

# PANTALLA 4: Videoteca Técnica
elif st.session_state.pantalla == 'videos':
    st.markdown('<div class="top-bar-jpl"><h2>REPOSITORIO L.I.N.A.</h2></div>', unsafe_allow_html=True)
    
    code_check = st.text_input("Ingrese código de verificación (Válido 15 días calendario):", type="password")
    
    if code_check == CODIGO_VIDEO_OK:
        st.success("Acceso autorizado (Incluye Sábados, Domingos y Festivos)")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Video de ejemplo
        st.write("📂 **Descargables asociados:** [Manual_SST.pdf] [Matriz_Riesgos.xlsx]")
    else:
        st.error("Código inválido o tiempo de acceso expirado.")

# --- 7. PIE DE PÁGINA INSTITUCIONAL ---
st.markdown(f"""
<div class="footer">
    © 2026 | L.I.N.A. V2.0 | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
