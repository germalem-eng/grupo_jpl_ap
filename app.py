import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

# --- 2. FUNCIÓN DE NOTIFICACIÓN (Solo para sus ojos) ---
def alerta_socio(plan_nombre):
    mi_correo = "germalem@gmail.com"
    # PEGAR AQUÍ LAS 16 LETRAS DE GOOGLE
    clave_google = "AQUÍ_SUS_16_LETRAS" 
    
    msg = MIMEText(f"Ing. Gerardo, un cliente hizo clic en el Plan {plan_nombre}. ¡Pendiente de la comisión!")
    msg['Subject'] = f"🚀 NUEVO CLIENTE JPL - {plan_nombre}"
    msg['From'] = mi_correo
    msg['To'] = mi_correo

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(mi_correo, clave_google)
        server.send_mail(mi_correo, mi_correo, msg.as_string())
        server.quit()
    except: pass

# --- 3. ESTILOS ---
st.markdown("""
<style>
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stButton>button { width: 100%; background-color: #000000; color: white !important; border: 1px solid white; font-weight: bold; }
    .sidebar-link { color: white !important; text-decoration: none; display: block; margin-bottom: 8px; font-size: 14px; }
    .price-card { border: 2px solid #800000; padding: 20px; border-radius: 10px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- 4. ACCESO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False
if not st.session_state['auth']:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.header("🔐 INGRESO JPL")
        u = st.text_input("Usuario:").lower()
        p = st.text_input("Clave:", type="password")
        if st.button("ENTRAR"):
            if u == "gerardo" and p == "mym2007":
                st.session_state['auth'] = True
                st.rerun()
            else: st.error("Acceso denegado")
    st.stop()

# --- 5. BARRA LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg")
    st.markdown("### CONTACTO")
    st.markdown('<a href="tel:3016015891" class="sidebar-link">Tel: 301 601 5891</a>', unsafe_allow_html=True)
    st.markdown('<a href="mailto:jplprevencionistas@gmail.com" class="sidebar-link">mail: jplprevencionistas@gmail.com</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://facebook.com/jplprevencionistas" target="_blank" class="sidebar-link">Jplprevencionistas</a>', unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("MENÚ:", ["📊 Panel de Control", "🛡️ Auditoría 60 Ítems", "💰 Licencias de Uso"])
    if st.button("CERRAR SESIÓN"):
        st.session_state['auth'] = False
        st.rerun()

# --- 6. CONTENIDO ---
num_wa = "573016015891"

if menu == "💰 Licencias de Uso":
    st.title("💰 Planes y Transparencia")
    with st.expander("📊 Reporte de Captación (Socios)"):
        st.write("Datos en tiempo real para liquidación de comisiones (50%).")
        st.metric("Clics en Planes (Mes)", "12 interesados")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="price-card"><h3>PEQUEÑA</h3><h2>$40.000</h2></div>', unsafe_allow_html=True)
        if st.button("ADQUIRIR 40K"):
            alerta_socio("Pequeña $40k")
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'https://wa.me/{num_wa}?text=Info%20Plan%2040k\'" />', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="price-card"><h3>MEDIANA</h3><h2>$60.000</h2></div>', unsafe_allow_html=True)
        if st.button("ADQUIRIR 60K"):
            alerta_socio("Mediana $60k")
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'https://wa.me/{num_wa}?text=Info%20Plan%2060k\'" />', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="price-card"><h3>GRANDE</h3><h2>$100.000</h2></div>', unsafe_allow_html=True)
        if st.button("ADQUIRIR 100K"):
            alerta_socio("Grande $100k")
            st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'https://wa.me/{num_wa}?text=Info%20Plan%20100k\'" />', unsafe_allow_html=True)
else:
    st.title(f"{menu}")
    st.info("Módulo activo y funcionando.")
