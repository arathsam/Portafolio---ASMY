import streamlit as st
import streamlit.components.v1 as components
import os
import base64

#----------Definicion de variables para tener todo mas estructurado.---------
#Diseño de la pagina
layout = "wide"
page_title = "Portafolio de Proyectos | ASMY"
page_icon = ":man_technologist:"

#------Variables para la descripcion del portafolio---------------------
profile_pic = "archivos/foto_perfil.jpg"
resume_file = "archivos/Resume_asmy.pdf"
resume_name = "ArathSamir_MuYee_Resume.pdf"

email = "arathyee09@gmail.com"
description = "Ingeniero Mecatrónico con experiencia en desarrollo de software, análisis de requerimientos y automatización de procesos en entornos industriales y tecnológicos. Experiencia desempeñando roles como Developer y Business Analyst, colaborando en la implementación de soluciones técnicas orientadas a negocio. Destaco por mi capacidad analítica, rápida adaptación y enfoque en la mejora continua."

#Leer el CV en PDF (en modo binario 'rb') Para tenerlo listo para descargar
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
#------------------------------------------------------------------------------------------------------------


#------------FUNCION PYTON CON HTML, Creamos una funcion para ajustar los items y mandarlos a imprimir con diseño en html----------------------------------------
languages_programacion = [
    "☕ Java", "🐍 Python", "⚡JavaScript", "⚙ C++","🗄️ SQL", "📱 Kotlin", "🎨 HTML/CSS"
]

def render_languages(title, langs):
    items = "".join([f"<li>{lang}</li>" for lang in langs])

    return f"""
    <div class="card_skills">
        <h3>{title}</h3>
        <ul>{items}</ul>
    </div>
    """

#-------------------------------------------------------------Backend Habilidades-----------------------------------------------------------------------------------------------------------
#--------------Habilidades - Arrays solo para iterar las posiciones e imprimirlas -------------------------
habilidades_tecnicas = [
    "Desarrollo Frond End con Python y Streamlit",
    "Manejo de estructuras de datos y lógica de programación",
    "Pruebas funcionales (QA básico)"]
skills_tech_html = "".join([f"<li>{stech}</li>" for stech in habilidades_tecnicas])


habilidades_profesionales = [
    "Adaptabilidad",
    "Aprendizaje continuo",
    "Trabajo bajo presión"
]
skills_prof_html = "".join([f"<li>{sprof}</li>" for sprof in habilidades_profesionales])

habilidades_competencias = [
    "Resolución de problemas",
    "Trabajo en equipo",
    "Análisis de requerimientos"
]
skills_html = "".join([f"<li>{slls}</li>" for slls in habilidades_competencias])

idiomas = [
    "Español - Nativo",
    "Ingles - B2"
]
languages_html = "".join([f"<p>{leng}</p>" for leng in idiomas])

#-------------------------------------------------------------Backend Barra de lenguajes-----------------------------------------------------------------------------------------------------------

languages_level= {
    "Java": 78,
    "Python": 74,
    "JavaScript": 70,
    "C++": 75,
    "SQL": 70,
    "Kotlin": 70,
    "HTML/CSS": 70
}

def render_languages_barlevel(title, level):
    items = ""

    for skill, levels in level.items():
        items += f"""
        <div class = "skill">
            <div class="skill-header"> 
                <span class="skill-name">{skill}</span>
                <span class="skill-hint">100%</span>
            </div>
            <div class = "bar">
                <div class="fill" data-width="{levels}"></div>
                <div class="bar-reference"></div>
            </div> 
            <div class="skill-note">Práctica Constante</div>
        </div>
        """
        
    html = f"""
    <style>
    .card, .card *{{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}

    .card {{
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0);
        transition: transform 0.5s ease, box-shadow 0.5s ease;
    }}

    .card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        background: linear-gradient(135deg, #d4e6ff, #ffffff);
        color: #2c5a7a;
        border: 1px solid rgba(76, 158, 237, 0.2);
    }}

    .card h3 {{
        margin: 0 0 12px 0;
        font-size: 1.2rem;
        font-weight: 600;
        color: #1e4a76;
    }}

    .skill {{
        margin-bottom: 10px;
    }}

    .skill-header {{
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 4px;
    }}

    .skill-name{{
        font-size: 14px;
        font-weight; 500;
        color: #2c5a7a;
    }}

    .skill-hint{{
        font-size: 11px;
        font-weight: 500;
        color: #94a3b8;
        letter-spacing: 0.3px;
    }}

    .bar {{
        position: relative;
        width: 100%;
        height: 8px;
        background-color: #e9ecef;
        border-radius: 10px;
        overflow: visible;
    }}

    .fill {{
        height: 100%;
        background: linear-gradient(90deg, #6fbf4c, #4cae3c);
        border-radius: 10px;
        width: 0%;
        transition: width 15s ease-out;
        position: relative;
        z-index: 2;
    }}

    .bar-reference{{
        position: absolute;
        top: 0;
        right: 0;
        width: 2px;
        height: 100%;
        background-color: #cbd5e1;
        border-radius: 2px;
        z-index: 1;
    }}

    .skill-note{{
        font-size: 12px;
        color: #2c5a7a;
        margin-top: 6px;
        font-style: italic;
        text-align: right;
    }}

    .skill-footer{{
        color: #2c5a7a;
        font-size: 15px;
    }}

    @keyframes grow {{
        from {{ width: 0; }}
        to {{width: var(--level); }}
    }}
    </style>

    <div class="card">
        <h3>{title}</h3>
        {items}
        <div class="skill-footer">
            <span>📚</span> Con documentación, practica y oportunidades, llego al 100%📚
        </div>
    </div>

     <script>
    (function() {{
        setTimeout(function() {{
            document.querySelectorAll('.fill').forEach(bar => {{
                const width = bar.getAttribute('data-width');
                bar.style.width = width + '%';
            }});
        }}, 100);
    }})();
    </script>
    """
    return html

#-------------------------------------------------------------Backend Proyectos-----------------------------------------------------------------------------------------------------------
projects = [
    {
        "title": "🌱 EcoFlow",
        "desc": "Sistema de riego inteligente controlado desde app Android, con monitoreo continuo mediante sensores, consulta de clima en tiempo real mediante APIs y comunicación Bluetooth con el dispositivo..",
        "tech": "Kotlin, C++, APIs, Bluetooth",
        "image": "archivos/logoriegohd.png",
        "link": "https://github.com/arathsam/EcoFlow.git"
    },
    {
        "title": "🎸 App de Aprendizaje Musical",
        "desc": "App Android para aprendizaje de instrumentos de cuerda con lecciones interactivas, simulación de guitarra, tablaturas de escalas y afinador digital basado en análisis de frecuencia.",
        "tech": "Java, XML, Android Studio",
        "image": "archivos/sonus_vester.jpg",
        "link": "https://github.com/arathsam')"
    },
    {
        "title": "🏋️ AppSport",
        "desc": "App Android que permitía actualizar y sincronizar rutinas de entrenamiento (WOD) de forma remota para usuarios durante la pandemia de COVID-19.",
        "tech": "Kotlin, XML, Android Studio",
        "image": "archivos/appsport.png",
        "link": "https://github.com/arathsam')" 

    },
    {
        "title": "📦 Sistema de Inventario",
        "desc": "Aplicación de escritorio para control de productos, actualización de existencias y registro de movimientos de inventario.",
        "tech": "Java, SQL",
        "image": "archivos/sistema_inventario.png",
        "link": "https://github.com/arathsam')"

    },
    {
        "title": "🏫 Sistema Escolar",
        "desc": "Sistema para registro de estudiantes, materias y consulta de información académica.",
        "tech": "Java, SQL",
        "image": "archivos/sistema_escolar.png",
        "link": "https://github.com/arathsam')"
    },
    {
        "title": "💳 Punto de Venta",
        "desc": "Aplicación para gestión de venta de articulos con registro de usuarios y control de disponibilidad mediante base de datos.",
        "tech": "JavaScript, SQL",
        "image": "archivos/punto_venta.png",
        "link": "https://github.com/arathsam')"
    }
]

#----------------------------------------Verifica si existe la imagen sino devuelve un fondo degradado----------------------------------------------------
def get_base64_image(path):
    import os
    import base64

    if not path or not os.path.exists(path):
        return None

    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_projects(projects):

    cards = ""

    #Duplicamos para efecto infinito
    loop_projects = projects*8

    for p in loop_projects:
        #Verificar si las imagenes existen, sino usar un fondo degradado
        #background = "linear-gradient(360deg, #87cffb, #f9d6a5)"
        
        img_base64 = get_base64_image(p.get("image"))
        if img_base64:
            image_html = f'<img src="data:image/png;base64,{img_base64}" />'
        else:
            image_html = '<div class="img-fallback"></div>'

        
        #Validar si tiene link o no los proyectos
        project_link = p.get('link', '')
        
        has_link = bool(project_link and project_link.strip() and project_link !='#')

        onclick = f"handleClick('{project_link}',this)"
        
        
        cards += f"""
        <div class="netflix-card" 
        onclick="{onclick}">
            <div class="img-top"> 
                {image_html}
            </div>
            <div class="content">
                <h3>{p['title']}</h3>
                <p>{p['desc']}</p>
                <span class="tech">Tecnologia: {p['tech']}</span>
                {'' if has_link else '<span class="soon-badge">🚀 Próximamente </span>'}
            </div>
        </div>
        """

    html = f"""
    <style>

    .container {{
        display: flex;
        gap: 20px;
        overflow-x: auto;
        padding: 20px;
        width: 100%;
        scroll-behavior: smooth;
        scroll-snap-type: x mandatory;
    }}

    .container:hover .track{{
        animation-play-state: paused;
    }}

    .track{{
        display: flex;
        gap: 20px;
        animation: scroll 320s linear infinite;
        cursor: pointer;
    }}


    .netflix-card {{
        flex: 0 0 250px;
        height: 300px;
        border-radius: 15px;
        overflow: hidden;
        display: flex;
        flex-direction: column;

        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
    }}

    .netflix-card:hover {{
        transform: scale(1.05) translateY(-5px);
        max-height: 100%;
        filter: brightness(1.08);

        z-index: 10;
    }}

    .img-top{{
        height: 140px;
        overflow: hidden;
        border-top-left-radius: 15px;
        border-top-right-radius: 15px;
    }}

    .img-top img{{
        width: 100%;
        height: 100%;
        object-fit: contain;
        background: linear-gradient(
            180deg,
            #c09a6c, 
            #f9d6a5
        );
    }}

    .netflix-card:hover .img-top{{
        transform: scale(1.05);
    }}
    
    .content{{
        background: linear-gradient(
            360deg,
            #c09a6c, 
            #f9d6a5
        );
        height: 160px;
        padding: 12px;

        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}

    @keyframes scroll{{
        0%{{
            transform: translateX(0);
        }}
        100%{{
            transform: translateX(-50%)
        }}
    }}

    .content h3 {{
        margin: 0;
        font-size: 16px;
        color: #1e4a76;
    }}

    .content p {{
        font-size: 14px;
        margin: 5px 0;
        color: #334155;
        line-height: 1.3;
    }}

    .tech {{
        font-size: 13px;
        color: #1e4a76;
    }}

    /*Scroll*/

    .container::-webkit-scrollbar-thumb {{
        background: #4c9eed;
        border-radius: 30px;
    }}

    .toast {{
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%) translateY(20px);
        background: linear-gradient(135deg, #1e4a76, #0f2c44);
        color: white;
        padding: 12px 24px;
        border-radius: 50px;
        font-size: 14px;
        font-weight: 500;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        opacity: 0;
        transition: all 0.3s ease;
        z-index: 99999;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255,255,255,0.2);
        pointer-events: none;
        white-space: nowrap;
    }}

    .toast.show {{
        opacity: 1;
        transform: translateX(-50%) translateY(0);
    }}
    
    </style>

    <div id="toast" class="toast">
        🚀 Proyecto próximamente en GitHub
    </div>

    <div class="container">
        <div class="track">
            {cards}
        </div>
    </div>

    <script>
    function showToast() {{
        const toast = document.getElementById("toast");
        toast.classList.add("show");
        
        setTimeout(() => {{
            toast.classList.remove("show");
        }}, 2500);
    }}

    function handleClick(link, element) {{
        if (link && link !== "" && link !== "#") {{
            window.open(link, "_blank");
        }} else {{
            showToast();
            // Efecto de vibración suave en la card
            event.currentTarget.style.transform = 'scale(0.98)';
            setTimeout(() => {{
                event.currentTarget.style.transform = '';
            }}, 150);
        }}
    }}
    </script>

    """

    return html

#---------------------------------------------------------------------------------------------------------------------------------


#------------- Experiencia Laboral - Arrays solo para iterar las posiciones e imprimirlas-----------------------------------------
nature_de_pain = [
    "Supervisión de turno y coordinación de personal operativo",
    "Soporte técnico en maquinaria industrial",
    "Diagnóstico y solución de fallas para asegurar la continuidad operativa",
    "Ajustes y mantenimiento básico de equipos en línea de producción"
]
#Lo convertimos en etiquepa li de html
nature_de_pain_html = "".join([f"<li>{ndp}</li>" for ndp in nature_de_pain])

hand_cloud = [
    "Desarrollo de Catalog Items en ServiceNow",
    "Levantamiento y análisis de requerimientos del negocio",
    "Creación y gestión de historias de usuario (Agile)",
    "Ejecución de pruebas funcionales (QA)",
    "Colaboración en equipos ágiles"
]
#Lo convertimos en etiquepa li de html
hand_cloud_html = "".join([f"<li>{hc}</li>" for hc in hand_cloud])

jabil_respons = [
    "Participación en proyectos de automatización industrial",
    "Desarrollo y soporte de soluciones técnicas",
    "Manejo y consulta de bases de datos",
    "Resolución de problemas en entornos productivos"
]
#Lo convertimos en etiquepa li de html
jabil_respons_html = "".join([f"<li>{j}</li>" for j in jabil_respons])

#-----------------------------------------------------------------------------------------------------------------







#------------------------------------Configuracion de la pagina----------------------------------
st.set_page_config(page_title=page_title, page_icon=page_icon, layout= layout)
st.markdown(
    """
    <style>
        /* ===== FONDO MODO OSCURO ===== */

        /* ===== CARDS - SIN FONDO POR DEFECTO ===== */
        .card, .card_jobs, .card_skills, .card_language {
            padding: 20px;
            border-radius: 15px;
            transition: transform 0.5s ease, box-shadow 0.5s ease, background 0.3s ease;
            background: transparent;
            box-shadow: none;
        }

        /* ===== HOVER - CUANDO EL CURSOR PASA ===== */
        .card:hover, .card_jobs:hover, .card_skills:hover, .card_language:hover {
            transform: translateY(-8px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }

        /* ===== CARD DESCRIPCIÓN - HOVER ===== */
        .card:hover {
            background: linear-gradient(135deg, #fce5c1, #fff0e0);
            color: #8b5a2b;
        }

        /* ===== CARD TRABAJOS - HOVER ===== */
        .card_jobs:hover {
            background: linear-gradient(135deg, #f3e5d8, #fdf8f2);
            color: #8b5a2b;
            transform: translateY(-8px) scale(1.02);
        }

        /* ===== CARD HABILIDADES - HOVER ===== */
        .card_skills:hover {
            background: linear-gradient(180deg, #d4e6ff, #ffffff);
            color: #1e4a76;
        }

        /* ===== CARD IDIOMAS - HOVER ===== */
        .card_language:hover {
            background: linear-gradient(360deg, #e0efff, #ffffff);
            color: #1e4a76;
        }

        /* ===== MODO OSCURO - CARDS SIN FONDO ===== */
        html[data-theme="dark"] .card,
        html[data-theme="dark"] .card_jobs,
        html[data-theme="dark"] .card_skills,
        html[data-theme="dark"] .card_language {
            background: transparent;
            color: #e2e8f0;
        }

        /* ===== MODO OSCURO - HOVER CON FONDO Y TEXTO NEGRO ===== */
        html[data-theme="dark"] .card:hover {
            background: linear-gradient(135deg, #fce5c1, #fff0e0);
            color: #000000 !important;
        }
        html[data-theme="dark"] .card:hover * {
            color: #000000 !important;
        }

        html[data-theme="dark"] .card_jobs:hover {
            background: linear-gradient(135deg, #f3e5d8, #fdf8f2);
            color: #000000 !important;
        }
        html[data-theme="dark"] .card_jobs:hover * {
            color: #000000 !important;
        }

        html[data-theme="dark"] .card_skills:hover {
            background: linear-gradient(180deg, #d4e6ff, #ffffff);
            color: #000000 !important;
        }
        html[data-theme="dark"] .card_skills:hover * {
            color: #000000 !important;
        }

        html[data-theme="dark"] .card_language:hover {
            background: linear-gradient(360deg, #e0efff, #ffffff);
            color: #000000 !important;
        }
        html[data-theme="dark"] .card_language:hover * {
            color: #000000 !important;
        }

        /* ===== TÍTULOS Y TEXTOS EN MODO OSCURO ===== */
        html[data-theme="dark"] h1,
        html[data-theme="dark"] h2,
        html[data-theme="dark"] h3,
        html[data-theme="dark"] h4,
        html[data-theme="dark"] p,
        html[data-theme="dark"] li {
            color: #e2e8f0;
        }

        /* ===== BARRAS DE PROGRESO MODO OSCURO ===== */
        html[data-theme="dark"] .bar {
            background-color: #334155 !important;
        }

        /* ===== SCROLLBAR MODO OSCURO ===== */
        html[data-theme="dark"] ::-webkit-scrollbar-track {
            background: #1e293b;
        }
        html[data-theme="dark"] ::-webkit-scrollbar-thumb {
            background: #4c9eed;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
#------------------------------------- HEADER PRINCIPAL -----------------------------------------------------------------------------------------------
st.markdown(
    """ 
        <div style = "text-align: center; margin-bottom: 20px;"> 
        <h1 class="card" style="color: #4c9eed; font-size: 2.5rem; margin-bottom: 10px;">
            Mi Portafolio 👨‍💻 Arath Samir Mu Yee
        </h1> 
        </div>
    """,unsafe_allow_html=True)

st.markdown(
    """
    <div class = "card" style = "text-align: center; margin-bottom: 25px;">
        <p style="font-size: 2rem; line-height: 1.5">
        📄 CV interactivo desarrollado con Python, HTML y Streamlit. 📄 <br>
        Explora mi experiencia, habilidades y proyectos.
        </p>
    </div>""",unsafe_allow_html=True)

#Creamos un directorio(HashMap) Para poder iterar el contenido directamente y redireccionar dependiendo de la posicion de los elementos dentro. (Usando su Key)
social_media = {
    "LinkedIn":"https://www.linkedin.com/in/arath-mu-yee/",
    "GitHub":"https://github.com/arathsam",
    "Indeed":"https://profile.indeed.com/?hl=es_MX&co=MX&from=gnav-homepage",
}

#Creamos un espacio
st.markdown("---")

#Descripcion del portafolio (Mi descripcion)
col1 , col2 = st.columns([1,1.2], gap="medium")

#Columna para poner de lado izquierdo
#Agregamos una separacion para centrar la imagen en la columna del lado izquierdo

with col1:
    #----------------------Centramos la foto d eperfil con efecto de bordes-----------------------
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 15px;">
            <div style="width: 180px; width: 180px; 
                height: 180px; 
                margin: 0 auto;
                border-radius: 50%;
                overflow: hidden;
                border: 3px solid #4c9eed;
                box-shadow: 0 8px 20px rgba(76, 158, 237, 0.2);
            </div>   
        </div>
        """, unsafe_allow_html=True)
    st.image(profile_pic, use_container_width=True)
    st.markdown("</div></div>",unsafe_allow_html=True)
    
    #-----------------Diseño y posicion de los botones---------------------------------
    st.markdown("""
    <style>
    .social-buttons {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 20px 0;
    }
    .social-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 20px;
        border-radius: 30px;
        text-decoration: none;
        font-weight: 500;
        font-size: 14px;
        transition: all 0.3s ease;
        background: #f0f4f9;
        color: #2c5a7a;
    }
    .social-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 14px rgba(0,0,0,0.1);
    }
    .social-btn.linkedin { background: #0077b5; color: white; }
    .social-btn.github { background: #333; color: white; }
    .social-btn.indeed { background: #2163b4; color: white; }
    </style>
    <div class="social-buttons">
        <a href="https://www.linkedin.com/in/arath-mu-yee/" target="_blank" class="social-btn linkedin">🔗 LinkedIn</a>
        <a href="https://github.com/arathsam" target="_blank" class="social-btn github">🐙 GitHub</a>
        <a href="https://profile.indeed.com/?hl=es_MX&co=MX&from=gnav-homepage" target="_blank" class="social-btn indeed">📄 Indeed</a>
    </div>
    """, unsafe_allow_html=True)

#--------------------Columna para poner de lado derecho-------------------------------------------------
with col2:
    st.markdown("""
    <div class="card" style="
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 20px;
    ">
        <h4 style=" font-size: 2rem; margin: 0 0 25px 0;">Acerca de mí</h4>
        <p style=" line-height: 1.6; margin: 0;">
            Ingeniero Mecatrónico con experiencia en desarrollo de software, análisis de requerimientos 
            y automatización de procesos en entornos industriales y tecnológicos. Destaco por mi capacidad 
            analítica, rápida adaptación y enfoque en la mejora continua.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_cv1, col_cv2, col_cv3 = st.columns([1, 1.5, 1])
    with col_cv2:
        st.download_button(
            label="📄 Descargar CV",
            data=PDFbyte,
            file_name=resume_name,
            use_container_width=True,
            type="primary"
        ) 

    #------------------Formulario para enviar el CV por correo-----------------------------------------------

    st.markdown("""
    <div style="margin-top: 20px; text-align: center;">
        <p style="color: #94a3b8; font-size: 20px; margin-bottom: 10px;">
            <br><br>📧 ¿Quieres recibir mi CV en tu correo?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form(key="email_form", clear_on_submit=True):
        col_email1, col_email2 = st.columns([2, 1])
        with col_email1:
            email_input = st.text_input("", placeholder="tu@correo.com", label_visibility="collapsed")
        with col_email2:
            submitted = st.form_submit_button("📨 Enviar", use_container_width=True)
        
        if submitted:
            if email_input and "@" in email_input:
                st.success(f"✅ ¡CV enviado a {email_input}! Revisa tu bandeja (y spam)")
                # Aquí puedes agregar la lógica real de envío de correo
            else:
                st.error("❌ Ingresa un correo válido")

#---------------------------------------------------------------------------------------------------------


#----Seccion de Habilidades-------------
st.write("---")
co1, co2, co3 = st.columns([1,2,1])
with co2:
    st.title("✨Habilidades✨")
    
st.markdown("---")
st.subheader("")

colum1, colum2, colum3 = st.columns(3)

#with colum1:
#    st.markdown("# ")
#    st.markdown("---")
#    st.subheader("💻 Técnicas")
#    st.write("#### Desarrollo / Programacion")
#    for habilidad in habilidades_tecnicas:
#        st.markdown(f"- {habilidad}")

with colum1:
    st.markdown(f""" 
                <div class="card_skills">
                
                ## 💻 Técnicas
                {skills_tech_html}
                </div>""", unsafe_allow_html=True)
    
with colum1:
    st.markdown(
        render_languages("💻 Lenguajes de Programación",languages_programacion), unsafe_allow_html=True
    )

with colum2:
    st.markdown(f""" 
                <div class="card_skills" style = "text-align: center">
                
                ## 🧠 Competencias
                {skills_html}
                </div>""", unsafe_allow_html=True)
    
    st.subheader("")
    st.markdown(f""" 
                <div class ="card_language" style = "text-align: center">
                
                ### 🌍 Idiomas
                {languages_html}
                </div>""", unsafe_allow_html=True)

with colum3:
    st.markdown(f""" 
                <div class="card_skills">
                
                ## 💼🤝Profesionales
                {skills_prof_html}
                </div> """,unsafe_allow_html=True)

    components.html(
        render_languages_barlevel("📊 Nivel de Habilidades", languages_level), 
        height=600)


#-----------------------------------------Seccion de Experiencia Laboral---------------------------------------- 
st.write("---")
co1, co2, co3 = st.columns([1,1,5])
with co3:
    st.title("💼 Experiencia Laboral 💼")
st.write("---")

colum1, colum2, colum3 = st.columns(3)

#with colum1:
#    st.markdown("---")
#    st.write("### 💻Business Analyst & ServiceNow Dev. Intern💼")
#    st.write("HandCloud | Zapopan, MX | 2024 – 2025")
#    for responsabilidades in hand_cloud:
#       st.markdown(f"- {responsabilidades}")
with colum1:
    st.markdown(f"""
                <div class = "card_jobs">

                ### 💻Business Analyst & ServiceNow Dev. Intern💼
                HandCloud | Zapopan, MX | 2024 – 2025
                {hand_cloud_html}
                </div>""",unsafe_allow_html=True)


#with colum2:
#    st.markdown("---")
#    st.write("### 🛠 Packing Shift Leader & Maintenance Support 📦")
#   st.write("Nature de Pain | Dublin, Ireland | 2025")
#  for responsabilidades in nature_de_pain:
#     st.markdown(f"- {responsabilidades}")
with colum2:
    st.markdown(f""" 
                <div class = "card_jobs">

                ### 🛠 Packing Shift Leader & Maintenance Support 📦
                Nature de Pain | Dublin, Ireland | 2025
                {nature_de_pain_html}
                </div>        
                """, unsafe_allow_html=True)


#with colum3:
#    st.markdown("---")
#    st.write("### ⚙ Lead Automation Engineer & Automation Intern🔨")
#    st.write("JABIL Circuit S.A. de C.V. | Zapopan, MX | 2021 – 2023")
#    for responsabilidades in jabil_respons:
#        st.markdown(f"- {responsabilidades}")

with colum3: 
    st.markdown(f"""
        <div class = "card_jobs">
        
        ### ⚙ Lead Automation Engineer & Automation Intern🔨
        JABIL Circuit S.A. de C.V. | Zapopan, MX | 2021 – 2023
        {jabil_respons_html}
        </div>""", unsafe_allow_html=True)

st.write("---")
co1, co2, co3 = st.columns([1,3,1])
with co2:
    st.title("🚀 Proyectos Escolares Destacados 💡")
st.write("---")

components.html(
    render_projects(projects),
    height=350
)
