import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="App JPL - Gestión SST", layout="wide", initial_sidebar_state="expanded")

# --- 2. BASE DE DATOS TÉCNICA (RESOLUCIÓN 0312 DE 2019) ---
# Listado completo de ítems según tamaño de empresa
E_7 = [
    "1.1.1 Asignación de persona que diseña el SG-SST",
    "1.1.3 Asignación de recursos para el SG-SST",
    "1.2.1 Afiliación al Sistema de Seguridad Social Integral",
    "2.1.1 Plan Anual de Trabajo",
    "4.1.1 Evaluación médica ocupacional",
    "6.1.1 Identificación de peligros, evaluación y valoración de riesgos",
    "7.1.1 Ejecución de medidas de prevención y control"
]

E_21 = [
    "1.1.1 Responsable", "1.1.3 Recursos", "1.1.5 COPASST", "1.1.6 Comité Convivencia",
    "1.2.1 Capacitación", "1.2.2 Inducción", "2.1.1 Plan Trabajo", "2.1.2 Archivo",
    "3.1.1 Sociodemográfico", "3.1.2 P&P", "3.1.4 Médicos", "3.1.9 Reporte AT/EL",
    "4.1.1 Peligros", "4.1.2 Mantenimiento", "4.1.3 EPP", "5.1.1 Emergencias",
    "6.1.1 Brigada", "6.1.4 Revisión Dirección", "7.1.1 Investigación AT",
    "7.1.2 Acciones Mejora", "7.1.3 Auditoría"
]

E_62 = {
    "RECURSOS (PLANEAR)": ["1.1.1 Responsable", "1.1.2 Responsabilidades", "1.1.3 Recursos", "1.1.4 Seg. Social", "1.1.5 COPASST", "1.1.6 Convivencia", "1.1.7 Capacitación", "1.1.8 Inducción", "1.2.1 Presupuesto", "1.2.2 Documentación", "1.2.3 Archivo"],
    "GESTIÓN SALUD (HACER)": ["3.1.1 Médicos", "3.1.2 Perfiles", "3.1.3 Historias", "3.1.4 Reporte AT/EL", "3.1.5 Investigación", "3.1.6 Matriz Peligros", "3.2.1 Higiene", "3.2.2 Estilos Vida"],
    "GESTIÓN PELIGROS (HACER)": ["4.1.1 Medidas", "4.1.2 Inspecciones", "4.1.3 Mantenimiento", "4.1.4 EPP", "4.1.5 Emergencias"],
    "GESTIÓN AMENAZAS (VERIFICAR/ACTUAR)": ["5.1.1 Planes Mejora", "5.1.2 Auditoría", "5.1.3 Revisión Dirección"]
}

# --- 3. ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Chilanka&display=swap');
    html, body, [class*="st-"], h1, h2, h3, p, label { font-family: 'Chilanka', cursive !important; }
    
    /* Sidebar Vinotinto */
    [data-testid="stSidebar"] { background-color: #800000; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* Botón INGRESAR (Gris Plata) */
    div.stButton > button:first-child {
        background-color: #C0C0C0 !important;
        color: #333 !important;
        border: 1px solid #A9A9A9;
        font-weight: bold;
    }

    /* Botón INICIO (Plata Brillante) */
    .btn-inicio button {
        background-color: #E5E4E2 !important;
        color: black !important;
        width: 100%;
    }

    .stApp { background-color: #F2F2F2; }
    
    .footer { 
        position: fixed; bottom: 0; left: 0; width: 100%; 
        background-color: #F2F2F2; text-align: center; 
        padding: 5px; font-size: 11px; border-top: 1px solid #800000; z-index: 100; 
    }

    .price-card { 
        background: white; padding: 20px; border-radius: 15px; 
        border: 2px solid #C0C0C0; text-align: center; 
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1); 
    }
    
    .card-item { 
        background: white; padding: 10px; border-radius: 8px; 
        border-left: 5px solid #800000; margin-bottom: 5px; 
    }
</style>
""", unsafe_allow_html=True)

# --- 4. LÓGICA DE RASTREO Y SESIÓN ---
if 'registro_uso' not in st.session_state: st.session_state.registro_uso = []
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'
if 'autenticado' not in st.session_state: st.session_state.autenticado = False

def rastrear(accion):
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.registro_uso.append({"Fecha": hora, "Acción": accion})

# --- 5. BARRA LATERAL (ACCESO Y NAVEGACIÓN) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    st.markdown("### ACCESO")
    
    if not st.session_state.autenticado:
        u = st.text_input("Usuario")
        p = st.text_input("Clave", type="password")
        if st.button("INGRESAR"):
            if u == "Gerardo" and p == "1234":
                st.session_state.autenticado = True
                rastrear("Login Exitoso: Gerardo")
                st.rerun()
            else:
                st.error("Credenciales incorrectas")
    else:
        st.success(f"Sesión: Gerardo")
        if st.button("SALIR"):
            st.session_state.autenticado = False
            rastrear("Cierre de Sesión")
            st.rerun()
    
    st.divider()
    st.markdown('<div class="btn-inicio">', unsafe_allow_html=True)
    if st.button("🏠 INICIO"): 
        st.session_state.pantalla = 'inicio'
        rastrear("Navegación: Inicio")
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("📊 ESTADÍSTICAS"): 
        st.session_state.pantalla = 'stats'
        rastrear("Navegación: Estadísticas")
        st.rerun()

    if st.button("🎥 VIDEOTECA"): 
        st.session_state.pantalla = 'videos'
        rastrear("Navegación: Videoteca")
        st.rerun()
    
    if st.session_state.autenticado:
        st.divider()
        st.markdown("🔒 **ADMIN JPL/MyM**")
        if st.button("👁️ RASTREO DE USO"): 
            st.session_state.pantalla = 'admin_logs'
            st.rerun()

# --- 6. PANTALLAS PRINCIPALES ---

# PANTALLA: INICIO Y PRECIOS
if st.session_state.pantalla == 'inicio':
    st.title("App JPL - Gestión Integral SST")
    
    st.markdown("### 💎 Planes Premium e Interés Comercial")
    c1, c2, c3, c4 = st.columns(4)
    planes = [
        ("Micro (<10)", "$30.000", "7 ítems", "573000000000"),
        ("Pyme (11-50)", "$60.000", "21 ítems", "573000000000"),
        ("Grande (>50)", "$100.000", "62 ítems", "573000000000"),
        ("Especial (+300)", "$300.000", "Full Gestión", "573000000000")
    ]
    
    for i, (nom, precio, detalle, tel) in enumerate(planes):
        with [c1, c2, c3, c4][i]:
            st.markdown(f"""<div class="price-card">
                <h4>{nom}</h4>
                <h2 style="color:#800000;">{precio}</h2>
                <p>{detalle}</p>
                <a href="https://wa.me/{tel}?text=Hola%20JPL,%20estoy%20interesado%20en%20el%20plan%20{nom}" target="_blank">
                <button style="background-color:#25D366; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer; font-weight:bold;">Verificar Interés</button>
                </a>
            </div>""", unsafe_allow_html=True)

    st.divider()
    st.subheader("Evaluación de Estándares Mínimos:")
    colA, colB, colC = st.columns(3)
    if colA.button("🏢 Evaluar Micro"): 
        st.session_state.nivel = "7"
        st.session_state.pantalla = 'auditoria'
        rastrear("Inicia Auditoría: Micro")
        st.rerun()
    if colB.button("🏬 Evaluar Pyme"): 
        st.session_state.nivel = "21"
        st.session_state.pantalla = 'auditoria'
        rastrear("Inicia Auditoría: Pyme")
        st.rerun()
    if colC.button("🏭 Evaluar Grande"): 
        st.session_state.nivel = "62"
        st.session_state.pantalla = 'auditoria'
        rastrear("Inicia Auditoría: Grande")
        st.rerun()

# PANTALLA: AUDITORÍA TÉCNICA
elif st.session_state.pantalla == 'auditoria':
    st.header(f"Auditoría Técnica: Nivel {st.session_state.nivel} Estándares")
    
    if st.session_state.nivel == "7": lista = E_7
    elif st.session_state.nivel == "21": lista = E_21
    else: lista = [item for sublist in E_62.values() for item in sublist]

    for item in lista:
        with st.container():
            st.markdown(f'<div class="card-item"><b>{item}</b></div>', unsafe_allow_html=True)
            col_eval, col_obs = st.columns([2, 1])
            cumple = col_eval.radio("Estado:", ["Pendiente", "CUMPLE", "NO CUMPLE", "NO APLICA"], key=item, horizontal=True, disabled=not st.session_state.autenticado)
            col_obs.text_input("Observaciones", key=f"obs_{item}", disabled=not st.session_state.autenticado)
            st.divider()

    if not st.session_state.autenticado:
        st.warning("⚠️ MODO LECTURA: El acceso de escritura es solo para Asociados Premium.")

# PANTALLA: ESTADÍSTICAS
elif st.session_state.pantalla == 'stats':
    st.header("📊 Panel de Estadísticas y Reportes")
    if st.session_state.autenticado:
        st.write("### Cumplimiento Normativo Actual")
        chart_data = pd.DataFrame(np.random.randint(40,100,size=(4, 1)), index=['Planear', 'Hacer', 'Verificar', 'Actuar'], columns=['% Cumplimiento'])
        st.bar_chart(chart_data)
        st.download_button("📥 Descargar Reporte Estadístico (PDF)", data="DATOS_PDF", file_name="Reporte_JPL.pdf")
    else:
        st.info("Gráficos de cumplimiento detallados disponibles para clientes asociados.")

# PANTALLA: VIDEOTECA
elif st.session_state.pantalla == 'videos':
    st.header("🎥 Videoteca L.I.N.A.")
    cod = st.text_input("Ingrese código de acceso (Válido 15 días corridos):", type="password")
    if cod == "JPL2026":
        st.success("Acceso Concedido (Incluye Sábados, Domingos y Festivos)")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        st.button("📥 Descargar Material Técnico")
    else:
        st.error("Se requiere código de verificación para visualizar el contenido.")

# PANTALLA: RASTREO (ADMIN)
elif st.session_state.pantalla == 'admin_logs':
    st.header("🕵️ Rastreo de Actividad (Vista Privada JPL/MyM)")
    if st.session_state.registro_uso:
        df_logs = pd.DataFrame(st.session_state.registro_uso)
        st.dataframe(df_logs, use_container_width=True)
    else:
        st.write("Aún no se ha registrado actividad en esta sesión.")

# --- 7. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
