import streamlit as st
import time

# --- 1. CONFIGURACIÓN Y BASE DE DATOS ---
st.set_page_config(page_title="L.I.N.A. | Grupo JPL", layout="centered", initial_sidebar_state="expanded")

# Usuarios con permiso de edición (Asociados/Premium)
usuarios_activos = {
    "gerardo@mym.com": "1234",
    "cliente@premium.com": "jpl2026"
}

# --- 2. ESTILOS CSS (Vinotinto, Chilanka y Marca de Agua) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }

    .stApp {
        background-color: #F2F2F2;
        background-image: url("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg");
        background-repeat: no-repeat; background-attachment: fixed; background-position: center; background-size: 55%;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(242, 242, 242, 0.96); z-index: -1;
    }

    .top-bar-jpl { background-color: #800000; padding: 20px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin: -65px -20px 25px -20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.3); }
    .card-proceso { background-color: rgba(255, 255, 255, 0.92); padding: 15px; border-radius: 20px; border-left: 10px solid #800000; margin-bottom: 15px; box-shadow: 0px 2px 8px rgba(0,0,0,0.1); }
    .stButton>button { background-color: #000000 !important; color: white !important; border-radius: 12px; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 3. ESTADO DE SESIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'splash'
if 'premium' not in st.session_state: st.session_state.premium = False

# --- 4. BARRA LATERAL (LOGIN SIEMPRE PRESENTE) ---
with st.sidebar:
    st.title("🔐 Mi Cuenta")
    if not st.session_state.premium:
        email = st.text_input("Correo asociado")
        password = st.text_input("Contraseña", type="password")
        if st.button("Validar Acceso"):
            if email in usuarios_activos and usuarios_activos[email] == password:
                st.session_state.premium = True
                st.rerun()
            else:
                st.error("Credenciales incorrectas")
    else:
        st.success("✅ Modo Premium Activo")
        if st.button("Cerrar Sesión"):
            st.session_state.premium = False
            st.rerun()

# --- 5. FUNCIÓN PARA MOSTRAR ÍTEMS CON BLOQUEO ---
def mostrar_item(codigo, descripcion):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**{codigo}** - {descripcion}")
    with col2:
        # Si no es premium, el selector está deshabilitado
        return st.selectbox("Estado", ["Pendiente", "Cumple", "No Cumple", "N/A"], 
                            key=codigo, disabled=not st.session_state.premium)

# --- 6. NAVEGACIÓN DE PANTALLAS ---

if st.session_state.pantalla == 'splash':
    st.markdown('<div style="text-align:center; margin-top:150px;">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=250)
    st.markdown("<h1 style='color:#800000; font-size:60px;'>L.I.N.A.</h1>", unsafe_allow_html=True)
    st.markdown("<p>Legalidad e Innovación en Normativa Aplicada</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    time.sleep(3)
    st.session_state.pantalla = 'inicio'
    st.rerun()

elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar-jpl"><h2>PROYECTO L.I.N.A.</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="card-proceso"><h3>SST - Grupo JPL</h3><p>Gestión avanzada de Estándares Mínimos (Res. 0312/2019)</p></div>', unsafe_allow_html=True)
    
    if st.button("🛡️ EVALUACIÓN TÉCNICA (SST)"):
        st.session_state.pantalla = 'sst'
        st.rerun()
    if st.button("💰 PLANES Y LICENCIAS"):
        st.session_state.pantalla = 'licencias'
        st.rerun()

elif st.session_state.pantalla == 'sst':
    st.markdown('<div class="top-bar-jpl"><h3>AUDITORÍA TÉCNICA</h3></div>', unsafe_allow_html=True)
    
    nivel = st.radio("Nivel de Empresa:", ["7 Ítems", "21 Ítems", "60 Ítems"], horizontal=True)
    
    if not st.session_state.premium:
        st.warning("⚠️ MODO VISTA PREVIA: Solo los clientes asociados pueden modificar los ítems.")
    
    st.markdown('<div class="card-proceso">', unsafe_allow_html=True)
    mostrar_item("1.1.1", "Responsable del Sistema")
    mostrar_item("1.1.3", "Asignación de Recursos")
    
    if "21 Ítems" in nivel or "60 Ítems" in nivel:
        mostrar_item("2.1.1", "Descripción Sociodemográfica")
    
    if "60 Ítems" in nivel:
        mostrar_item("4.1.1", "Plan de Emergencias")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.premium:
        if st.button("💾 GUARDAR CAMBIOS"):
            st.balloons()
            st.success("Guardado exitoso.")

elif st.session_state.pantalla == 'licencias':
    st.markdown('<div class="top-bar-jpl"><h3>SOLUCIONES PREMIUM</h3></div>', unsafe_allow_html=True)
    st.write("Para activar el modo edición, contacta a Soluciones MyM.")
    if st.button("⬅️ VOLVER AL MENÚ"):
        st.session_state.pantalla = 'inicio'
        st.rerun()

# --- BARRA INFERIOR ---
if st.session_state.pantalla != 'splash':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        if st.button("🏠"): st.session_state.pantalla = 'inicio'; st.rerun()
    with cols[1]:
        if st.button("🛡️"): st.session_state.pantalla = 'sst'; st.rerun()
    with cols[2]:
        if st.button("📊"): st.info("Reportes próximamente")
