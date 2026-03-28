import streamlit as st

#-----------------------CLASE PARA DISEÑO--------------------------
#DESCRIPCION
st.markdown("""
<style>
.card {
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0);
    transition: transform 0.5s ease, box-shadow 0.5s ease;
}
.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    background-color: #FFFFFF;
}
</style>
""", unsafe_allow_html=True)

#TRABAJOS
st.markdown("""
<style>
.card_jobs{
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0);
    transition: transform 0.5s ease, box-shadow 0.5s ease;
}
.card_jobs:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    background-color: #F0FDF4;
}
</style>
""", unsafe_allow_html=True)

#HABILIDADES
st.markdown("""
<style>
.card_skills{
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0);
    transition: transform 0.5s ease, box-shadow 0.5s ease;
}
.card_skills:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    background-color: #EEF1F5;
}
</style>
""", unsafe_allow_html=True)

#IDIOMAS
st.markdown("""
<style>
.card_language{
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0);
    transition: transform 0.5s ease, box-shadow 0.5s ease;
}
.card_language:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    background-color: #EEF2FF;
}
</style>
""", unsafe_allow_html=True)

#----------------------------------------


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


#--------------Habilidades - Arrays solo para iterar las posiciones e imprimirlas -------------------------
habilidades_tecnicas = [
    "Java | JavaScript | C++ | SQL | Kotlin | HTML/CSS",
    "Desarrollo Frond End con Python y Streamlit",
    "Manejo de estructuras de datos y lógica de programación"]
skills_tech_html = "".join([f"<li>{stech}</li>" for stech in habilidades_tecnicas])

habilidades_profesionales = [
    "Trabajo en equipo",
    "Adaptabilidad",
    "Aprendizaje continuo",
    "Trabajo bajo presión"
]
skills_prof_html = "".join([f"<li>{sprof}</li>" for sprof in habilidades_profesionales])

habilidades_competencias = [
    "Resolución de problemas",
    "Análisis de requerimientos",
    "Pruebas funcionales (QA básico)"
]
skills_html = "".join([f"<li>{slls}</li>" for slls in habilidades_competencias])

idiomas = [
    "Español - Nativo",
    "Ingles - B2"
]
languages_html = "".join([f"<p>{leng}</p>" for leng in idiomas])
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


#-------Configuracion de la pagina---------
st.set_page_config(page_title=page_title, page_icon=page_icon, layout= layout)

st.markdown(""" 
            <div style = "text-align: center;"> 
            <h1>Mi Portafolio 👨‍💻 Arath Samir Mu Yee</h1> 
            </div>
            """,unsafe_allow_html=True)

st.markdown("""
            <div class = "card" 
            style = "text-align: center;">
            <H4>Este sitio es mi currículum web interactivo desarrollado con Python y Streamlit,
            donde presento mi experiencia, habilidades y proyectos de forma dinámica.
            </H4>
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
col1 , col2 = st.columns(2)

#Columna para poner de lado izquierdo
#Agregamos una separacion para centrar la imagen en la columna del lado izquierdo
with col1:
    with st.container():
        c1, c2, c3 = st.columns([1,2,1])
    with c2:  
        st.write("""
            <div style = "text-align: center" > 
            
             ### Mis perfiles & Historial de Proyectos
             </div>""",unsafe_allow_html=True)
  
        st.image(profile_pic, use_container_width=True)

        #Cols es basicamente para obtener las posiciones del directorio 
        #Creamos los botones para redireccionar a las 'redes sociales'
        cols = st.columns(len(social_media))
        for it, (name_sm, url) in enumerate(social_media.items()):
            with cols[it]:
                st.link_button(name_sm, 
                            url,
                            help="Click para ir a la pagina",
                            type="primary")
    

#--------------------Columna para poner de lado derecho-------------------------------------------------
with col2:
    st.write("## Acerca de mi")
    st.write(f"""
             <div class="card">
             
             <p >{description}</p>
             </div>""", unsafe_allow_html=True)
    st.download_button(
        label="📃 Descargar CV", #Texto que mostrará el boton
        data= PDFbyte, #El archivo la leido y combertido en bytes
        file_name=resume_name, #Nombre de como se va a guardar el archivo descargado
        type="primary", #El tipo de boton
        icon=":material/download:" #mMuestra el icono de descargable
    )    

#---------------------------------------------------------------------------------------------------------


#----Seccion de Habilidades-------------
st.write("---")
colum1, colum2, colum3 = st.columns(3)
with colum2:
    st.title("✨Habilidades✨")
    st.markdown("---")

#with colum1:
#    st.markdown("# ")
#    st.markdown("---")
#    st.subheader("💻 Técnicas")
#    st.write("#### Desarrollo / Programacion")
#    for habilidad in habilidades_tecnicas:
#        st.markdown(f"- {habilidad}")

with colum1:
    st.markdown("# ")
    st.markdown("---")
    st.markdown(f""" 
                <div class="card_skills">
                
                ## 💻 Técnicas
                {skills_tech_html}
                </div>""", unsafe_allow_html=True)

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
    st.markdown("# ")
    st.markdown("---")
    st.markdown(f""" 
                <div class="card_skills">
                
                ## 💼🤝Profesionales
                {skills_prof_html}
                </div> """,unsafe_allow_html=True)




#-----------------------------------------Seccion de Experiencia Laboral---------------------------------------- 
st.write("---")
st.title("💼 Experiencia Laboral 💼")

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



