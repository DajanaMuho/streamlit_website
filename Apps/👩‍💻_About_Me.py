import streamlit as st
from PIL import Image

# RUN: streamlit run 👩‍💻_About_Me.py

st.set_page_config(
    page_title="DM",
    page_icon="👋",
    layout="wide", #centered,
    menu_items={
        "Get Help": 'https://www.linkedin.com/in/dajanamuho/',
        'About': ''' 
            # Welcome, 
            Portofolio of Dajana Muho
        '''
    }
)

image = Image.open('/home/dajana/Dropbox/Photos/DSC_5378.jpg')

col1, col2 = st.columns(2)

with col1:
    st.header("# Get to know me! 👋")
    st.image(image, width = 250)

with col2:
    st.header("")
    st.header("")
    st.subheader("# Dajana Muho")
    st.write("#### Data Scientist | Full Stack Engineer")
    st.write(" 🏠  New York, USA")
    st.write(" 📩  [dajana_muho@yahoo.com](dajana_muho@yahoo.com)")
    st.write(" 📞  (+1) 779 270 4311")
    st.write(" 🔗  [LinkedIn](https://www.linkedin.com/in/dajanamuho/)")
    st.write(" 🖥  [GitHub](https://github.com/DajanaMuho)")



st.markdown(
    """
   Complex problem-solver with an analytical and driven mindset. Graduated as an excellent student with a BS degree in Computer Science. 
   Currently pursuing an MS in Data Science. Experienced at creating machine learning models, using predictive data modeling, 
   and analyzing data mining algorithms to deliver insights and implement action-oriented solutions to complex business problems. 
   Collaborative team player with excellent technical abilities offering 3+ years of full-stack engineer experience. 
   Relevant skills include machine learning, problem-solving, programming, and creative thinking. 
   Motivated to learn, grow and excel.
   
    ### SKILLS
    * Programming experience in **Python**, **JavaScript**, **Node.js**, **React.js**, **Hadoop**, **SPARK**, **Microservices**.
    * Designed, developed, and deployed **Machine Learning** and **Deep Learning** models.
    * Expertise in database development and implementation using **MongoDB**, **MySQL**, **Redis**, **Oracle**.
    * Develop data pipelines to **Google Cloud Platform** and transform data in **Google Big Query**.
    * Good knowledge in **Data Analysis** and **Data Visualization** using **Tableau** and **Google Data Studio**.
    * Familiar with **Neuro- Linguistics Programming (NLP)**.
    * Proficiency with **Data Mining**, **Algorithms and Data Structures**.
    * Thorough understanding of **Software Development Life Cycle** and **Big Data Life Cycle**.
    * Knowledge in **Unified Modeling Language (UML)**.
    
    ### EDUCATION
    **Master of Science**: Data Science _(Expected to May 2023)_ \n
    _Graduate Center, City University of New York, New York_ \n
    **GPA**: 4.00/4.00
    \n \n \n \n \n \n
    **Bachelor of Science**: Computer Science _(July 2019)_ \n
    _University of Tirana, Albania_ \n
    **GPA**: 3.86/4.00
    
    ### HOBBIES & INTERESTS
    * Travel
    * Photography
    * Technology    
    * Volunteering
    * Dance
    """
)