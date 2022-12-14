import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Projects",
    page_icon="π",
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
    neural_model_img = Image.open('Apps/images/graph.png')
    cos_img = Image.open('Apps/images/cosine.png')
    video_file = open('Apps/images/video_screen_area.mp4', 'rb')
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
            β Extract the tokens from string of characters.\n
            β Lemmatize the words by returning the base form of the words, and lower casing.\n
            β Convert data to numerical values by using the technique Bag Of Words for easy use in modeling.\n
            
          * **Split training dataset** \n
            β Source: [Microsoft Research WikiQA Corpus](https://www.microsoft.com/en-us/download/details.aspx?id=52419) \n
            β Split into features which we will consider βPatternβ and labels are βTagβ which we will predict.
           
          * **Build Deep Learning Model** \n
            β Sequential model with some dropout layers which prevent from overο¬tting to data. Used relu and sotfmax as activations. \n
            β Train the model
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
    video_file = open('Apps/images/Project Demo.mp4', 'rb')
    st.video(video_file.read(), "video/mp4", 80)

    col1, col2 = st.columns(2)
    with col1:
        architecture = Image.open("Apps/images/Insurance Management System.png")
        st.image(architecture, width=250, use_column_width=True)
    with col2:
        ml = Image.open("Apps/images/ml.png")
        st.image(ml, width=250, use_column_width=True)


if selected_project == 'Big Data Analysis Using Python':
    st.header("# [Sentiment Analysis on the tweets about distance learning](https://github.com/DajanaMuho/Sentiment-Analysis)")
    st.write("**Build a machine learning model to predict the positivity and the negativity of the tweets, to help the education system identify the best learning approach.**")
    pos = 'Apps/images/positive.png'
    neg = 'Apps/images/negative.png'
    country = 'Apps/images/country.png'

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
            β Check for missing values\n
            β Fill missing values\n
            β Drop uninformative columns\n
            β Remove duplicates\n
            β Convert data types\n

          * **Exploratory Data Analysis** \n
            β Investigation on data\n
            β Discover patterns\n
            β Visualize the data\n
            """
        )
        st.image(country, width=250, use_column_width=True)
    with col2:
        st.markdown(
            """
        * **Feature Engineering** \n
            β Remove links\n
            β Remove mentions and hashtag\n
            β Tokenize the words by splitting into small units\n
            β Remove stop words that doesnβt add much meaning to a sentence\n
            β Lemmatize the words \n
            β Remove non-alphabetic characters\n
            β Select the features and the target labels\n
        
        * **Sentiment Analysis** \n
            β Calculate polarity and subjectivity\n
            
            
        * **Machine Learning Models** \n
            β Encode the polarity labels\n
            β Split the dataset into 20% validation data and 80% training data\n
            β Vectorize data\n
            β Fit the model\n
            β Predict\n
            β Compare accuracy between the machine learning algorithms to choose the best fit
            """
        )

if selected_project == 'Data Visualization':
    st.header("# [U.S Immigration Trends](https://github.com/DajanaMuho/Data-Visualization)")
    world_mape_img = Image.open('Apps/images/Graph_1_World_Map.png')
    line_graph = 'Apps/images/Graph_2_Line_Trend.gif'
    dream_gif = 'Apps/images/Graph_3_Pie_Vide.mp4'

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
    workflow ="Apps/images/workflow.png"
    data = "Apps/images/data.png"
    text = "Apps/images/text.png"

    st.image(workflow, use_column_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image(data, use_column_width=True)
    with col2:
        st.image(text, use_column_width=True)