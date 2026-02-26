import streamlit as st
from datetime import datetime, timedelta

# CONFIGURACIÓN
st.set_page_config(
    page_title="Dashboard Quirófano - Keralty",
    page_icon="🏥",
    layout="wide"
)

# -------- ESTILOS PERSONALIZADOS --------
st.markdown("""
<style>

/* Fondo azul turquí corporativo */
.stApp {
    background: linear-gradient(135deg, #00b4d8, #0096c7, #0077b6);
    background-attachment: fixed;
}

/* Quitar fondo blanco interno */
section.main > div {
    background-color: transparent !important;
}

/* Header */
.header {
    background: rgba(255, 255, 255, 0.15);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    backdrop-filter: blur(6px);
}

/* Tarjetas estilo glass */
.card {
    background: rgba(255, 255, 255, 0.18);
    backdrop-filter: blur(12px);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    transition: 0.3s ease-in-out;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 12px 30px rgba(0,0,0,0.3);
}

/* Etiquetas */
.label {
    font-size: 18px;
    color: white;
    margin-bottom: 10px;
    font-weight: 600;
}

/* Números grandes degradado azul fuerte */
.number {
    font-size: 60px;
    font-weight: bold;
    background: linear-gradient(90deg, #03045e, #023e8a, #0077b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Estado OK */
.status-ok {
    font-size: 44px;
    font-weight: bold;
    background: linear-gradient(90deg, #00ffcc, #00cc99);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Estado atraso */
.status-delay {
    font-size: 44px;
    font-weight: bold;
    color: #ff3b3b;
}

/* Texto general blanco */
div, label {
    color: white !important;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 40px;
    color: white;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown('<div class="header">🏥 QUIRÓFANO 3 - KERALTY S.A</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------- LOGO --------
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Keralty_logo.svg/2560px-Keralty_logo.svg.png", width=220)

st.markdown("<br><br>", unsafe_allow_html=True)

# -------- INPUTS --------
col1, col2 = st.columns(2)

with col1:
    hora_inicio = st.time_input("Hora Inicio Cirugía", value=datetime.now().time())

with col2:
    duracion_estimada = st.number_input("Duración estimada (minutos)", min_value=30, max_value=600, value=90)

# -------- CÁLCULOS --------
fecha_actual = datetime.now().date()
inicio_datetime = datetime.combine(fecha_actual, hora_inicio)
hora_fin_estimada = inicio_datetime + timedelta(minutes=duracion_estimada)
hora_actual = datetime.now()

atraso = hora_actual > hora_fin_estimada

# -------- TARJETAS --------
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="label">Hora Inicio</div>
        <div class="number">{inicio_datetime.strftime("%H:%M:%S")}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="label">Quirófano</div>
        <div class="number">3</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="label">Hora Estimada Fin</div>
        <div class="number">{hora_fin_estimada.strftime("%H:%M:%S")}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    if atraso:
        st.markdown("""
        <div class="card">
            <div class="label">Estado Cirugía</div>
            <div class="status-delay">⚠ ATRASADO</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card">
            <div class="label">Estado Cirugía</div>
            <div class="status-ok">✔ A TIEMPO</div>
        </div>
        """, unsafe_allow_html=True)

# -------- HORA ACTUAL --------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div style='text-align:center; font-size:22px;'>
Hora actual: <b>{hora_actual.strftime("%H:%M:%S")}</b>
</div>
""", unsafe_allow_html=True)

# -------- FOOTER --------
st.markdown('<div class="footer">Sistema Inteligente de Control Quirúrgico - Keralty S.A</div>', unsafe_allow_html=True)
