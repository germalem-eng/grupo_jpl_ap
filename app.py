import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Grupo JPL | Gestión SST", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
<style>
    [data-testid="stSidebar"] { background-color: #800000 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #800000; }
    .phva-circle {
        width: 80px; height: 80px; background-color: #800000;
        color: white; border-radius: 50%; display: flex;
        align-items: center; justify-content: center;
        font-size: 28px; font-weight: bold; margin: 0 auto;
    }
</style>
""", unsafe_allow_html=True)

# --- CONTROL DE ACCESO ---
if 'auth' not in st.session_state: st.session_state['auth'] = False

if not st.session_state['auth']:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<div style='text-align:center; padding:30px; border:2px solid #800000; border-radius:15px;'>", unsafe_allow_html=True)
        st.header("🔐 INGRESO GRUPO JPL")
        u = st.text_input("Usuario:").lower()
        p = st.text_input("Contraseña:", type="password")
        if st.button("ACCEDER"):
            if u == "gerardo" and p == "mym2007":
                st.session_state['auth'] = True
                st.rerun()
            else: st.error("Acceso denegado")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- NAVEGACIÓN LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg")
    st.markdown("---")
    menu = st.radio("MENÚ DE GESTIÓN:", ["📊 Panel de Control", "🛡️ Auditoría 60 Ítems", "💰 Licencias de Uso"])
    if st.button("🚪 CERRAR SESIÓN"):
        st.session_state['auth'] = False
        st.rerun()

# --- CONTENIDO INTERACTIVO ---

if menu == "📊 Panel de Control":
    st.title("📊 Panel de Control Interactivo")
    
    # Indicadores en tiempo real (Interactivos)
    col_a, col_b, col_c = st.columns(3)
    with col_a: st.metric("Cumplimiento Legal", "85%", "+2%")
    with col_b: st.metric("Accidentalidad", "0", "-5%")
    with col_c: st.metric("Capacitación", "92%", "Activo")

    st.markdown("---")
    st.subheader("🔄 Ciclo PHVA - Gestión de Tareas")
    
    # Aquí la línea de tiempo deja de ser una diapositiva y tiene botones
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="phva-circle">P</div>', unsafe_allow_html=True)
        if st.button("Ver Plan de Trabajo"): st.write("✅ Cargando actividades planeadas...")
    with c2:
        st.markdown('<div class="phva-circle">H</div>', unsafe_allow_html=True)
        if st.button("Registrar Evidencia"): st.file_uploader("Subir PDF/Imagen")
    with c3:
        st.markdown('<div class="phva-circle">V</div>', unsafe_allow_html=True)
        if st.button("Ver Indicadores"): st.line_chart([10, 25, 30, 45])
    with c4:
        st.markdown('<div class="phva-circle">A</div>', unsafe_allow_html=True)
        if st.button("Acciones Correctivas"): st.text_area("Describa la mejora necesaria:")

elif menu == "🛡️ Auditoría 60 Ítems":
    st.title("🛡️ Autoevaluación Estándares Mínimos")
    st.info("Complete los ítems para calcular el porcentaje de cumplimiento.")
    
    # Formulario interactivo
    with st.form("auditoria_sst"):
        i1 = st.selectbox("1. ¿Cuenta con Responsable del SG-SST?", ["Cumple", "No Cumple", "No Aplica"])
        i2 = st.selectbox("2. ¿Existe Política de SST firmada?", ["Cumple", "No Cumple", "No Aplica"])
        i3 = st.selectbox("3. ¿Se realizó la Identificación de Peligros?", ["Cumple", "No Cumple", "No Aplica"])
        
        enviar = st.form_submit_button("CALCULAR RESULTADO")
        if enviar:
            st.success("Auditoría guardada exitosamente.")
            st.progress(66) # Ejemplo de barra de progreso

elif menu == "💰 Licencias de Uso":
    st.title("💰 Planes de Licenciamiento")
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.markdown("<div style='border:2px solid #800000; padding:20px; border-radius:10px; text-align:center;'><h3>Pyme</h3><h2>$40.000</h2><p>1-10 emp.</p></div>", unsafe_allow_html=True)
        if st.button("Contratar 40k"): st.link_button("Ir a WhatsApp", "https://wa.me/573016015891")
    # (Repetir para los otros precios)
