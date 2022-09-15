import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Projects",
    page_icon="📁",
    layout="wide" #centered,

)

selected_project = st.sidebar.radio(
    '',
    ('Machine Learning',
     'Storage, Retrieval, and Processing of Big Data',
     'Big Data Analysis Using Python',
     'Data Visualization',
     'Data Mining'
     )
)

if selected_project == 'Machine Learning':
    st.header("# [ROBO-CHAT](https://github.com/DajanaMuho/Robo-Chat)")
    neural_model_img = Image.open('/home/dajana/Dropbox/CUNY/Machine Learning/Project/Robo-Chat/graph.png')
    cos_img = Image.open('/home/dajana/Dropbox/CUNY/Machine Learning/Project/Robo-Chat/cosine.png')
    video_file = open('/home/dajana/Dropbox/CUNY/Machine Learning/Project/Robo-Chat/video_screen_area.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes, "video/mp4", 14)
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Neural Network Approach")
        st.image(neural_model_img, width=250, use_column_width=True)
        st.markdown("\n\n\n\n\n\n")
        st.write("### Cosine Similarity Approach")
        st.markdown(
            """
            Similarity between 0 and 1 \n
            1 = Most Similar Sentence\n
            0 = Least Similar Sentence\n
            HIGHEST SIMILARITY = BEST RESPONSE\n
            """
        )
        st.write("###### DEMO: https://youtu.be/gQ3TM_JdOfY")

    with col2:
        st.markdown(
            """
          * **Apply pre-processing** \n
            → Extract the tokens from string of characters.\n
            → Lemmatize the words by returning the base form of the words, and lower casing.\n
            → Convert data to numerical values by using the technique Bag Of Words for easy use in modeling.\n
            
          * **Split training dataset** \n
            → Source: [Microsoft Research WikiQA Corpus](https://www.microsoft.com/en-us/download/details.aspx?id=52419) \n
            → Split into features which we will consider ‘Pattern’ and labels are ‘Tag’ which we will predict.
           
          * **Build Deep Learning Model** \n
            → Sequential model with some dropout layers which prevent from overﬁtting to data. Used relu and sotfmax as activations. \n
            → Train the model
           """
        )
        st.markdown("###### DEMO: https://youtu.be/umnWtlQdKFI")
        st.markdown("\n\n\n\n\n\n")
        st.image(cos_img, width=250, use_column_width=True)


if selected_project == 'Storage, Retrieval, and Processing of Big Data':
    st.header('# [Insurance Management System](https://github.com/DajanaMuho/Insurance-Management-System)')
    st.markdown(
        """
        **To empower the insurance companies by providing:**
        * _The analytics of the driver behavior_\n
        * _ML-Models to share the potential claim behavior_\n
        * _Full stack management system to visualize the driver behavior_.
        """
    )
    video_file = open('/home/dajana/Dropbox/WMU/Classes/Big Data/Project Demo.mp4', 'rb')
    st.video(video_file.read(), "video/mp4", 80)

    col1, col2 = st.columns(2)
    with col1:
        architecture = Image.open(
            "/home/dajana/Dropbox/WMU/Classes/Big Data/Project/Insurance Management System.png")
        st.image(architecture, width=250, use_column_width=True)
    with col2:
        ml = Image.open("/home/dajana/Dropbox/WMU/Classes/Big Data/Project/ml.png")
        st.image(ml, width=250, use_column_width=True)


if selected_project == 'Big Data Analysis Using Python':
    st.header("# [Sentiment Analysis on the tweets about distance learning](https://github.com/DajanaMuho/Sentiment-Analysis)")
    st.write("**Build a machine learning model to predict the positivity and the negativity of the tweets, to help the education system identify the best learning approach.**")
    pos = '/home/dajana/Dropbox/WMU/Classes/Big Data Analysis Using Python/Project/positive.png'
    neg = '/home/dajana/Dropbox/WMU/Classes/Big Data Analysis Using Python/Project/negative.png'
    country = '/home/dajana/Dropbox/WMU/Classes/Big Data Analysis Using Python/Project/country.png'

    col1, col2 = st.columns(2)
    with col1:
        st.image(pos, width=250, use_column_width=True)
        st.write("_Common words in the positive tweets_")

    with col2:
        st.image(neg, width=250, use_column_width=True)
        st.write("_Common words in the negative tweets_")

    st.write('## Workflow')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
          * **Data Gathering** \n
            Source: [Kaggle Dataset](https://www.kaggle.com/datasets/barishasdemir/tweets-about-distance-learning)

          * **Data Preparation** \n
            → Check for missing values\n
            → Fill missing values\n
            → Drop uninformative columns\n
            → Remove duplicates\n
            → Convert data types\n

          * **Exploratory Data Analysis** \n
            → Investigation on data\n
            → Discover patterns\n
            → Visualize the data\n
            """
        )
        st.image(country, width=250, use_column_width=True)
    with col2:
        st.markdown(
            """
        * **Feature Engineering** \n
            → Remove links\n
            → Remove mentions and hashtag\n
            → Tokenize the words by splitting into small units\n
            → Remove stop words that doesn’t add much meaning to a sentence\n
            → Lemmatize the words \n
            → Remove non-alphabetic characters\n
            → Select the features and the target labels\n
        
        * **Sentiment Analysis** \n
            → Calculate polarity and subjectivity\n
            
            
        * **Machine Learning Models** \n
            → Encode the polarity labels\n
            → Split the dataset into 20% validation data and 80% training data\n
            → Vectorize data\n
            → Fit the model\n
            → Predict\n
            → Compare accuracy between the machine learning algorithms to choose the best fit
            """
        )

if selected_project == 'Data Visualization':
    st.header("# [U.S Immigration Trends](https://github.com/DajanaMuho/Data-Visualization)")
    world_mape_img = Image.open('/home/dajana/Dropbox/CUNY/Data Visualization/Project/Graph_1_World_Map.png')
    line_graph = '/home/dajana/Dropbox/CUNY/Data Visualization/Project/Graph_2_Line_Trend.gif'
    dream_gif = '/home/dajana/Dropbox/CUNY/Data Visualization/Project/Graph_3_Pie_Vide.mp4'

    st.image(world_mape_img, use_column_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.write('## Design Process')
        st.markdown(
            """
            * ##### Formulating the brief\n\n
            * ##### Establishing editorial thinking\n\n
            * ##### Working with data\n\n
            * ##### Develop Design Solution\n
        """
        )
    with col2:
        video_file = open(dream_gif, 'rb')
        st.video(video_file.read(), "video/mp4")

    st.image(line_graph, width=250, use_column_width=True)



if selected_project == 'Data Mining':
    st.header("# [Hospital Readmission Prediction](https://github.com/DajanaMuho/hospital-readmission)")
    st.write('## Goals')
    st.markdown(
        """
        * To implement machine learning models to predict if the patient will be readmitted to the hospital.\n
        * To improve the efficiency of healthcare services. 
    """
    )
    workflow ="/home/dajana/Dropbox/CUNY/Machine Learning/HW/workflow.png"
    data = "/home/dajana/Dropbox/CUNY/Machine Learning/HW/data.png"
    text = "/home/dajana/Dropbox/CUNY/Machine Learning/HW/text.png"

    st.image(workflow, use_column_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image(data, use_column_width=True)
    with col2:
        st.image(text, use_column_width=True)