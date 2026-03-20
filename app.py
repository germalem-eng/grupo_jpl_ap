import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- 1. CONFIGURACIÓN Y ESTILOS ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stButton>button { width: 100%; background-color: #000000; color: white !important; border: 1px solid white; font-weight: bold; }
    .sidebar-link { color: white !important; text-decoration: none; display: block; margin-bottom: 8px; font-size: 14px; }
    .price-card { border: 2px solid #800000; padding: 20px; border-radius: 10px; text-align: center; background-color: white; height: 100%; }
    .phva-circle { width: 70px; height: 70px; background-color: #800000; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; margin: 0 auto; border: 2px solid black; }
</style>
""", unsafe_allow_html=True)

# --- 2. FUNCIÓN DE NOTIFICACIÓN OCULTA ---
def alerta_socio(plan_nombre):
    mi_correo = "germalem@gmail.com"
    clave_google = "CLAVE_DE_16_LETRAS" # <--- CAMBIE ESTO POR SUS 16 LETRAS
    msg = MIMEText(f"Ing. Gerardo, un cliente se interesó en: {plan_nombre}")
    msg['Subject'] = f"🚀 ALERTA SOCIO: {plan_nombre}"
    msg['From'] = mi_correo
    msg['To'] = mi_correo
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(mi_correo, clave_google)
        server.sendmail(mi_correo, mi_correo, msg.as_string())
        server.quit()
    except: pass

# --- 3. ACCESO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False
if not st.session_state['auth']:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br><div style='text-align:center; border:2px solid #800000; padding:20px; border-radius:15px;'>", unsafe_allow_html=True)
        st.header("🔐 SISTEMA JPL")
        u = st.text_input("Usuario:").lower()
        p = st.text_input("Clave:", type="password")
        if st.button("ENTRAR"):
            if u == "gerardo" and p == "mym2007":
                st.session_state['auth'] = True
                st.rerun()
            else: st.error("Acceso denegado")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg")
    st.markdown("### CONTACTO OFICIAL")
    st.markdown('<a href="tel:3016015891" class="sidebar-link">Tel: 301 601 5891</a>', unsafe_allow_html=True)
    st.markdown('<a href="mailto:jplprevencionistas@gmail.com" class="sidebar-link">mail: jplprevencionistas@gmail.com</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://facebook.com/jplprevencionistas" target="_blank" class="sidebar-link">Jplprevencionistas</a>', unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("MÓDULOS:", ["📊 Panel de Control", "🛡️ Auditoría 60 Ítems", "💰 Licencias de Uso"])
    if st.button("CERRAR SESIÓN"):
        st.session_state['auth'] = False
        st.rerun()

# --- 5. CONTENIDO POR MÓDULO ---
num_wa = "573016015891"

if menu == "📊 Panel de Control":
    st.title("📊 Gestión Continua PHVA")
    st.info("Bienvenido, Ing. Gerardo. Aquí puede gestionar los avances del SG-SST.")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="phva-circle">P</div><p style="text-align:center"><b>PLANEAR</b></p>', unsafe_allow_html=True)
        if st.button("Definir Plan"): st.success("✅ Cronograma 2026 listo.")
    with c2:
        st.markdown('<div class="phva-circle">H</div><p style="text-align:center"><b>HACER</b></p>', unsafe_allow_html=True)
        st.file_uploader("Evidencias (PDF/JPG)")
    with c3:
        st.markdown('<div class="phva-circle">V</div><p style="text-align:center"><b>VERIFICAR</b></p>', unsafe_allow_html=True)
        if st.button("Resultados"): st.line_chart([10, 20, 15, 30])
    with c4:
        st.markdown('<div class="phva-circle">A</div><p style="text-align:center"><b>ACTUAR</b></p>', unsafe_allow_html=True)
        st.text_area("Acciones de Mejora:")

elif menu == "🛡️ Auditoría 60 Ítems":
    st.title("🛡️ Auditoría Resolución 0312")
    st.write("Evalúe los estándares mínimos para conocer el nivel de cumplimiento.")
    with st.form("audit"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.selectbox("1. Asignación de recursos", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("2. Afiliación al Sistema SS", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("3. Conformación de COPASST", ["Cumple", "No Cumple", "N/A"])
        with col_f2:
            st.selectbox("4. Programa de capacitación", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("5. Evaluación médica", ["Cumple", "No Cumple", "N/A"])
            st.selectbox("6. Identificación de Peligros", ["Cumple", "No Cumple", "N/A"])
        if st.form_submit_button("GUARDAR Y CALCULAR"):
            st.success("Auditoría procesada. Nivel de ejecución: 78%")

elif menu == "💰 Licencias de Uso":
    st.title("💰 Planes de Afiliación")
    with st.expander("📊 Reporte de Captación (Exclusivo Gerardo)"):
        st.metric("Prospectos Mes", "12", "50% comisión activa")

    col_1, col_2, col_3 = st.columns(3)
    planes = [("PEQUEÑA", "40.000"), ("MEDIANA", "60.000"), ("GRANDE", "100.000")]
    
    for i, (nombre, precio) in enumerate(planes):
        with [col_1, col_2, col_3][i]:
            st.markdown(f'<div class="price-card"><h3>{nombre}</h3><h2>${precio}</h2></div>', unsafe_allow_html=True)
            if st.button(f"ADQUIRIR {nombre}"):
                alerta_socio(f"{nombre} ${precio}")
                st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'https://wa.me/{num_wa}?text=Deseo%20el%20Plan%20{nombre}\'" />', unsafe_allow_html=True)
