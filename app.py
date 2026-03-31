import streamlit as st
import time

# --- CONFIGURACIÓN ESTILO WOM ---
st.set_page_config(page_title="L.I.N.A. | MyM", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }

    /* Color Principal Estilo WOM (Morado/Azul) */
    .stApp { background-color: #FFFFFF; }
    
    /* Barra Superior Curva */
    .header-wom {
        background-color: #60269e; /* Morado WOM */
        padding: 30px;
        border-radius: 0 0 40px 40px;
        color: white;
        text-align: center;
        margin: -75px -20px 20px -20px;
    }

    /* Tarjetas tipo "Mi Plan" */
    .card-wom {
        background-color: #f4f0fa;
        padding: 20px;
        border-radius: 25px;
        border: 1px solid #e0d5f2;
        margin-bottom: 15px;
        text-align: center;
    }

    /* Botón Circular Central (como el de la foto) */
    .main-button {
        background-color: #60269e;
        color: white;
        border-radius: 50%;
        width: 80px;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        box-shadow: 0 4px 15px rgba(96, 38, 158, 0.4);
    }

    /* Barra de Navegación Inferior Blanca con iconos */
    .nav-bottom {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: white;
        padding: 10px 0;
        display: flex;
        justify-content: space-around;
        border-top: 1px solid #ddd;
        z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVEGACIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'splash'

if st.session_state.pantalla == 'splash':
    st.markdown('<div style="text-align:center; margin-top:150px;">', unsafe_allow_html=True)
    # Aquí irá tu logo circular de L.I.N.A.
    st.image("https://raw.githubusercontent.com/germalem-eng/lina-app/main/foto_logo_jpl.jpg", width=200)
    st.markdown("<h1 style='color:#60269e;'>L.I.N.A.</h1>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    time.sleep(3)
    st.session_state.pantalla = 'inicio'
    st.rerun()

elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="header-wom"><h1>L.I.N.A.</h1><p>Soluciones MyM</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card-wom"><h3>MI PROYECTO</h3><p>Gestión 2026 - Activa</p></div>', unsafe_allow_html=True)
    
    # Botones de acción rápida
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🛡️ AUDITORÍA"): st.session_state.pantalla = 'sst'; st.rerun()
    with col2:
        if st.button("📊 REPORTES"): st.info("Cargando...")

    # Simulación del botón central circular de tu foto
    st.markdown('<br><div class="main-button">🔍</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:12px;'>EXPLORAR</p>", unsafe_allow_html=True)

# --- BARRA INFERIOR (ESTILO TU CAPTURA) ---
if st.session_state.pantalla != 'splash':
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    cols = st.columns(5)
    with cols[0]: st.button("🏠", key="nav1")
    with cols[1]: st.button("🎁", key="nav2")
    with cols[2]: st.button("📱", key="nav3")
    with cols[3]: st.button("📶", key="nav4")
    with cols[4]: st.button("❓", key="nav5")
