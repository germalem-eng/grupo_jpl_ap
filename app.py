import streamlit as st
import time
import smtplib
from email.mime.text import MIMEText

# --- 1. CONFIGURACIÓN Y ESTILOS ---
st.set_page_config(page_title="Grupo JPL SST", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }
    .stApp { background-color: #F2F2F2; }
    
    /* Splash Logo */
    .logo-splash { display: block; margin: auto; width: 250px; opacity: 0.8; animation: fadeIn 2s; }
    @keyframes fadeIn { from {opacity: 0;} to {opacity: 0.8;} }

    /* Contenedores Estilo App */
    .top-bar-jpl { background-color: #800000; padding: 20px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin: -65px -20px 25px -20px; }
    .card-proceso { background-color: white; padding: 15px; border-radius: 20px; box-shadow: 0px 2px 8px rgba(0,0,0,0.05); margin-bottom: 15px; border-left: 10px solid #800000; }
    .box-amenazas-jpl { background-color: #BEBEBE; padding: 15px; border-radius: 20px; border: 2px solid #800000; margin-bottom: 15px; color: black; }
    
    /* Barra navegación inferior fija */
    .footer-nav { position: fixed; bottom: 0; left: 0; width: 100%; background: white; border-top: 2px solid #800000; padding: 10px 0; z-index: 100; }
</style>
""", unsafe_allow_html=True)

# --- 2. LÓGICA DE NAVEGACIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'splash'

def cambiar_pantalla(nombre):
    st.session_state.pantalla = nombre

# --- 3. PANTALLA: SPLASH ---
if st.session_state.pantalla == 'splash':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<img src="https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg" class="logo-splash">', unsafe_allow_html=True)
    time.sleep(2)
    cambiar_pantalla('inicio')
    st.rerun()

# --- 4. PANTALLA: INICIO ---
elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar-jpl"><h2>GRUPO JPL</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="card-proceso"><h3>Estado General</h3><p>Resolución 0312 de 2019</p></div>', unsafe_allow_html=True)
    
    st.subheader("Accesos Directos")
    if st.button("🛡️ INICIAR AUDITORÍA 60 ÍTEMS"): cambiar_pantalla('sst') ; st.rerun()
    if st.button("💰 VER PLANES DE AFILIACIÓN"): cambiar_pantalla('licencias') ; st.rerun()

# --- 5. PANTALLA: SST (60 ÍTEMS) ---
elif st.session_state.pantalla == 'sst':
    st.markdown('<div class="top-bar-jpl"><h3>ESTÁNDARE MÍNIMOS</h3></div>', unsafe_allow_html=True)
    
    with st.form("audit_60"):
        st.markdown('<div class="card-proceso"><h4>I, II, III: RECURSOS, SALUD Y RIESGOS</h4>', unsafe_allow_html=True)
        # Aquí irían los bloques de ítems del 1 al 42
        st.selectbox("1.1.1. Responsable del SG-SST", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("1.2.1. Programa de Capacitación", ["Cumple", "No Cumple", "N/A"])
        st.selectbox("3.1.1. Identificación de Peligros", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="box-amenazas-jpl"><h4>IV. AMENAZAS (Ítems 43-47)</h4>', unsafe_allow_html=True)
        st.radio("43. Plan de Emergencias", ["Cumple", "No Cumple"], horizontal=True)
        st.radio("46. Simulacros anuales", ["Cumple", "No Cumple"], horizontal=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card-proceso"><h4>V, VI, VII: VERIFICACIÓN Y MEJORA</h4>', unsafe_allow_html=True)
        st.selectbox("60. Plan de mejoramiento", ["Cumple", "No Cumple", "N/A"])
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.form_submit_button("GUARDAR AUDITORÍA"): st.success("Guardado")

# --- 6. PANTALLA: LICENCIAS (LOS 3 PLANES) ---
elif st.session_state.pantalla == 'licencias':
    st.markdown('<div class="top-bar-jpl"><h3>PLANES DE USO</h3></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card-proceso" style="border-left:5px solid black;"><b>PEQUEÑA</b><br>$40.000</div>', unsafe_allow_html=True)
        if st.button("Elegir 40k"): st.write("📞 Contactando...")
    with col2:
        st.markdown('<div class="card-proceso"><b>MEDIANA</b><br>$60.000</div>', unsafe_allow_html=True)
        if st.button("Elegir 60k"): st.write("📞 Contactando...")
    with col3:
        st.markdown('<div class="card-proceso" style="border-left:5px solid grey;"><b>GRANDE</b><br>$100.000</div>', unsafe_allow_html=True)
        if st.button("Elegir 100k"): st.write("📞 Contactando...")

# --- BARRA DE NAVEGACIÓN INFERIOR (BOTONES FUNCIONALES) ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
with st.container():
    cols = st.columns(3)
    with cols[0]:
        if st.button("🏠 INICIO"): cambiar_pantalla('inicio') ; st.rerun()
    with cols[1]:
        if st.button("🛡️ SST"): cambiar_pantalla('sst') ; st.rerun()
    with cols[2]:
        if st.button("📊 REPORTE"): cambiar_pantalla('inicio') ; st.rerun()
