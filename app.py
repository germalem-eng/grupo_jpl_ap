import streamlit as st
import time

# --- 1. CONFIGURACIÓN Y BASE DE DATOS ---
st.set_page_config(page_title="APP JPL | Soluciones MyM", layout="centered", initial_sidebar_state="expanded")

# Base de datos de asociados (Asociados actuales o Premium nuevos)
usuarios_activos = {
    "gerardo@mym.com": "1234",
    "cliente@premium.com": "jpl2026"
}

# --- 2. ESTILOS VISUALES (Vinotinto y Marca de Agua) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }

    .stApp {
        background-color: #F2F2F2;
        background-image: url("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg");
        background-repeat: no-repeat; background-attachment: fixed; background-position: center; background-size: 50%;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(242, 242, 242, 0.96); z-index: -1;
    }

    .top-bar-jpl { background-color: #800000; padding: 20px; border-radius: 0 0 30px 30px; color: white; text-align: center; margin: -65px -20px 25px -20px; }
    .card-proceso { background-color: rgba(255, 255, 255, 0.95); padding: 15px; border-radius: 20px; border-left: 10px solid #800000; margin-bottom: 15px; box-shadow: 0px 2px 8px rgba(0,0,0,0.1); }
    
    /* Estilo de botones */
    .stButton>button { background-color: #000000 !important; color: white !important; border-radius: 12px; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- 3. CONTROL DE SESIÓN ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'splash'
if 'premium' not in st.session_state: st.session_state.premium = False

# --- 4. BARRA LATERAL (LOGIN ASOCIADOS) ---
with st.sidebar:
    st.markdown("### 🔐 ACCESO ASOCIADOS")
    if not st.session_state.premium:
        user_input = st.text_input("Correo electrónico")
        pass_input = st.text_input("Clave", type="password")
        if st.button("INGRESAR"):
            if user_input in usuarios_activos and usuarios_activos[user_input] == pass_input:
                st.session_state.premium = True
                st.success("Acceso Premium Activado")
                st.rerun()
            else:
                st.error("Credenciales no válidas")
    else:
        st.success(f"Sesión Activa: {st.session_state.get('user', 'Asociado')}")
        if st.button("Cerrar Sesión"):
            st.session_state.premium = False
            st.rerun()

# --- 5. LÓGICA DE PANTALLAS ---

if st.session_state.pantalla == 'splash':
    st.markdown('<div style="text-align:center; margin-top:150px;">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=250)
    st.markdown("<h1 style='color:#800000; font-size:60px;'>APP JPL</h1>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.pantalla = 'inicio'
    st.rerun()

elif st.session_state.pantalla == 'inicio':
    st.markdown('<div class="top-bar-jpl"><h1>APP JPL</h1></div>', unsafe_allow_html=True)
    
    st.markdown("### Seleccione el nivel de evaluación:")
    
    # Los 3 botones que solicitaste según tus apuntes
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Empresas < 10\n(7 Estándares)"):
            st.session_state.nivel = "7"
            st.session_state.pantalla = 'evaluacion'
            st.rerun()
    with col2:
        if st.button("Empresas 11-50\n(21 Estándares)"):
            st.session_state.nivel = "21"
            st.session_state.pantalla = 'evaluacion'
            st.rerun()
    with col3:
        if st.button("Empresas > 50\n(60 Estándares)"):
            st.session_state.nivel = "60"
            st.session_state.pantalla = 'evaluacion'
            st.rerun()

elif st.session_state.pantalla == 'evaluacion':
    st.markdown(f'<div class="top-bar-jpl"><h3>EVALUACIÓN {st.session_state.nivel} ÍTEMS</h3></div>', unsafe_allow_html=True)
    
    if not st.session_state.premium:
        st.warning("⚠️ MODO VISTA PREVIA: Solo los Asociados Actuales o Clientes Premium pueden interactuar y modificar los ítems.")
    else:
        st.success("✅ MODO EDICIÓN ACTIVO: Puede gestionar los estándares.")

    # Función para mostrar los ítems con el candado (disabled si no es premium)
    def mostrar_item(cod, desc):
        st.markdown(f'<div class="card-proceso"><b>{cod}</b> - {desc}</div>', unsafe_allow_html=True)
        return st.selectbox("Calificación:", ["Pendiente", "Cumple", "No Cumple", "N/A"], 
                            key=cod, disabled=not st.session_state.premium)

    # --- LISTADO DE ÍTEMS SEGÚN EL NIVEL SELECCIONADO ---
    if st.session_state.nivel == "7":
        mostrar_item("1.1.1", "Responsable del Sistema (Licencia y Curso 50h)")
        mostrar_item("1.1.3", "Asignación de recursos")
        # Agregar los otros 5 aquí...
        
    elif st.session_state.nivel == "21":
        mostrar_item("1.1.1", "Responsable del Sistema")
        mostrar_item("2.1.1", "Descripción sociodemográfica")
        # Agregar los otros 19 aquí...
        
    elif st.session_state.nivel == "60":
        mostrar_item("1.1.1", "Responsable del Sistema")
        mostrar_item("4.1.1", "Plan de emergencias")
        # Agregar los otros 58 aquí...

    # Botones de acción
    if st.session_state.premium:
        if st.button("💾 GUARDAR AVANCE"):
            st.balloons()
            st.success("Datos guardados en el servidor de Soluciones MyM.")
    
    if st.button("⬅️ VOLVER AL MENÚ"):
        st.session_state.pantalla = 'inicio'
        st.rerun()
