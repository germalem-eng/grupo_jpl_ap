import streamlit as st
import time
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="App JPL", layout="wide", initial_sidebar_state="expanded")

# --- 2. BASE DE DATOS TÉCNICA (RESOLUCIÓN 0312 DE 2019) ---
E_7 = ["1.1.1 Responsable", "1.1.3 Recursos", "1.2.1 Seguridad Social", "2.1.1 Plan Trabajo", "4.1.1 Médicos", "6.1.1 Peligros", "7.1.1 Medidas Control"]
E_21 = ["Responsable", "Recursos", "COPASST", "Comité Convivencia", "Capacitación", "Inducción", "Plan Trabajo", "Archivo", "Sociodemográfico", "P&P", "Médicos", "Reporte AT/EL", "Peligros", "Mantenimiento", "EPP", "Emergencias", "Brigada", "Revisión Dirección", "Investigación AT", "Acciones Mejora", "Auditoría"]

# --- 3. ESTILOS CSS (Botones Gris Plata y Sidebar Vinotinto) ---
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
    }

    .stApp { background-color: #F2F2F2; }
    .footer { position: fixed; bottom: 0; left: 0; width: 100%; background-color: #F2F2F2; text-align: center; padding: 5px; font-size: 11px; border-top: 1px solid #800000; z-index: 100; }
    .price-card { background: white; padding: 20px; border-radius: 15px; border: 2px solid #C0C0C0; text-align: center; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# --- 4. LÓGICA DE RASTREO (Solo para JPL y MyM) ---
if 'registro_uso' not in st.session_state:
    st.session_state.registro_uso = []

def rastrear(accion):
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.registro_uso.append({"Fecha": hora, "Acción": accion})

# --- 5. BARRA LATERAL ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/germalem-eng/grupo_jpl_ap/main/Logos/foto_logo_jpl.jpg", width=120)
    st.markdown("### ACCESO")
    if 'autenticado' not in st.session_state: st.session_state.autenticado = False
    
    if not st.session_state.autenticado:
        u = st.text_input("Usuario")
        p = st.text_input("Clave", type="password")
        if st.button("INGRESAR"):
            if u == "Gerardo" and p == "1234":
                st.session_state.autenticado = True
                rastrear("Login Exitoso: Gerardo")
                st.rerun()
    else:
        st.success(f"Sesión: Gerardo")
        if st.button("SALIR"):
            st.session_state.autenticado = False
            st.rerun()
    
    st.divider()
    st.markdown('<div class="btn-inicio">', unsafe_allow_html=True)
    if st.button("🏠 INICIO"): 
        st.session_state.pantalla = 'inicio'
        rastrear("Navegación: Inicio")
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("📊 ESTADÍSTICAS"): st.session_state.pantalla = 'stats'; st.rerun()
    
    # Vista Privada JPL/MyM
    if st.session_state.autenticado:
        st.divider()
        st.markdown("🔒 **ADMIN JPL/MyM**")
        if st.button("👁️ RASTREO DE USO"): st.session_state.pantalla = 'admin_logs'; st.rerun()

# --- 6. PANTALLAS ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'

if st.session_state.pantalla == 'inicio':
    st.title("App JPL - Servicios Premium")
    
    # Sección de Precios Premium
    st.markdown("### 💎 Planes Premium (Res. 0312 de 2019)")
    c1, c2, c3, c4 = st.columns(4)
    
    planes = [
        ("Micro (<10)", "$30.000", "7 ítems"),
        ("Pyme (11-50)", "$60.000", "21 ítems"),
        ("Grande (>50)", "$100.000", "62 ítems"),
        ("Especial (>300)", "$300.000", "Full Gestión")
    ]
    
    for i, (nom, precio, detalle) in enumerate(planes):
        with [c1, c2, c3, c4][i]:
            st.markdown(f"""<div class="price-card">
                <h4>{nom}</h4>
                <h2 style="color:#800000;">{precio}</h2>
                <p>{detalle}</p>
                <a href="https://wa.me/573000000000?text=Hola%20JPL,%20estoy%20interesado%20en%20el%20plan%20{nom}" target="_blank">
                <button style="background-color:#25D366; color:white; border:none; padding:10px; border-radius:5px; cursor:pointer;">Verificar Interés</button>
                </a>
            </div>""", unsafe_allow_html=True)

    st.divider()
    st.subheader("Seleccione evaluación técnica:")
    colA, colB, colC = st.columns(3)
    if colA.button("Evaluar Micro"): st.session_state.pantalla = 'auditoria'; st.session_state.nivel = "7"; rastrear("Selección: Micro"); st.rerun()
    if colB.button("Evaluar Pyme"): st.session_state.pantalla = 'auditoria'; st.session_state.nivel = "21"; rastrear("Selección: Pyme"); st.rerun()
    if colC.button("Evaluar Grande"): st.session_state.pantalla = 'auditoria'; st.session_state.nivel = "62"; rastrear("Selección: Grande"); st.rerun()

elif st.session_state.pantalla == 'admin_logs':
    st.header("🕵️ Rastreo de Actividad (Solo JPL/MyM)")
    if st.session_state.registro_uso:
        df_logs = pd.DataFrame(st.session_state.registro_uso)
        st.table(df_logs)
    else:
        st.write("No hay actividad registrada aún.")

# (Otras pantallas de auditoría y estadísticas se mantienen como en la versión anterior)

# --- 7. PIE DE PÁGINA ---
st.markdown(f"""
<div class="footer">
    © 2026 | App JPL | Proyecto L.I.N.A. | Desarrollado por Ing. Gerardo Martinez Lemus | <b>JPL Prevencionistas SAS</b>
</div>
""", unsafe_allow_html=True)
