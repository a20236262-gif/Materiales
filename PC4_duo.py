# python -m venv .venv
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1
# python -m streamlit hello
# python -m streamlit run PC4_duo.py

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

### Opción 1: Menú vertical
with st.sidebar:
    opciones = option_menu("Secciones: ",['Presentación', 'Experiencia', 'Gráficos'] , 
        # personalizar los íconos
        # icons (secciones)
        # menu_icons (icono del menú)
        # link de repositorio de iconos: https://icons.getbootstrap.com 
        icons=['people-fill','1-circle', '2-circle'], menu_icon="people-fill", default_index=0)

### Opción 2: Menú vertical
# opciones_2 = option_menu(
    # menu_title="Selecciona una sección: ", 
    # options=['Presentación', 'Experiencia', 'Gráficos'], 
    # icons=['0-circle','1-circle', '2-circle'], 
    # menu_icon="cast", default_index=0, orientation="horizontal")

# contenido de la PRIMERA SECCIÓN ()
if opciones == 'Presentación':
    #encabezado 
    # <h1>: de encabezado
    # 'text align': para centrar
    # Nombre del blog (editar!)
    # unsafe_allow_html=True: permite editar
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Blog informático</h1>", unsafe_allow_html=True)

    # Alumno a
    # (2): indica el número de columnas, no posición
    col1, col2 = st.columns(2)

    # Caption: etiqueta debajo de la foto
    col1.image("Foto_Ariana.jpg", caption='Ariana', width=300)

    # 3 comillas para los textos
    texto = """
    Este blog pertenece a Ariana Jáuregui Rojas, estudiante de Publicidad en la PUCP. 
    Tengo 22 años y voy a mitad de la carrera. Me considero una persona con diferentes intereses y curiosidad por aprender. 
    Por ello, el curso Pensamiento Computacional me interesa, porque el lenguaje de programación es 
    algo que no había aprendido antes. Además de lo académico, uno de mis hobbies es el karate. 
    Deporte que empecé a inicios de año y hoy ya me encuentro como cinturón celeste raya amarilla, un nivel novel aún. 
    Del karate rescato la disciplina y persistencia que este deporte me ayudó a desarrollar. 
    """
    # markdown: personaliza el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;color: black'>{texto}</div>", unsafe_allow_html=True)

    # Alumno b
    col1, col2 = st.columns(2)
    
    texto_2 = """
    Aquí escribe una presentación creativa sobre ti.
    ¿Quién eres? 
    ¿De dónde eres? 
    ¿Qué estudias? 
    ¿Qué te gusta de tu carrera? 
    ¿Qué te gustaría hacer en el futuro? 
    ¿Qué te gusta hacer en tu tiempo libre?
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)
    
    col2.image("Foto_Ariana.jpg", caption='Adriana', width=300)

 # SEGUNDA SECCIÓN (Experiencia)   
elif  opciones == 'Experiencia':
    # Nombre a la sección de experiencia 💻 (personalizar !)
    # lista de emogis: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nombre a la sección de experiencia 💻</h1>", unsafe_allow_html=True)

    # Alumno a
    texto_3 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio? 
    ¿Qué te ha enseñado la programación? 
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)
    
    # Formato YouTube (previsualización en la página)
    # st.subheader("🎥 Título apropiado video 1")
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    
    # Formato Google Drive (botón)
    # copiar por cada video
    st.subheader("🎥 Título apropiado video 2")

    # Para centrar un botón:
    # creamos 3 columnas (col1, col2, col3)
    # ([1, 2, 1]): asigna tamaño a las columnas
    col1, col2, col3 = st.columns([1, 2, 1])

    # contenido del botón
    with col2:  
        st.link_button("🎥 Texto del botón",
                       # link como string
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
            )
    # Aqui acaba el formato drive

    # Alumno b
    texto_4 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio?
    ¿Qué te ha enseñado la programación?
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
             )

# TERCERA SECCIÓN (gráficos)           
else:
    # encabezado principal
    # (Nombre a la sección) editar!
    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nombre a la sección</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    # 10 en total (3 gráficos + 1 mapa) por integrante
    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    
    if grafico_seleccionado == 'Gráfico_1':
        # sibtitulo de gráfico
        st.subheader("Nube de palabras: Reunión en el Restaurante Nostalgia")
        texto_5 = """
        Interpretación del Gráfico 1 (editar!)
        """
        # formato
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)
        # para centrar
        col1, col2, col3 = st.columns([1, 9, 1])
        with col2:
                st.image("Wordcloud.png", width=800)
    # continuar con más elif (8 elif)
    elif grafico_seleccionado == 'Gráfico_2':
        st.subheader("📊 Gráfico 2: Familias lingüísticas")
        texto_6 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("lengua_familia_GB.png", width=800)
    
    else:
        st.subheader("🗺️ Mapa 1: Distribución geográfica")
        texto_7 = """
        Interpretación del mapa
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)
        #  "r", encoding="utf-8": no editar    
        with open("mapa_base.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    