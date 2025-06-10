from gettext import install
from pdb import run
import pip
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import joblib

# Load Data
df = pd.read_csv(r"C:\Users\manoj\Desktop\job_market\job_market.csv")  # Update path as needed

# Load Encoders


with open(r"C:\Users\manoj\Desktop\job_market\Job_Title_encoding.pkl", 'rb') as f:
    Job_Title_encoding = pickle.load(f)
with open(r"C:\Users\manoj\Desktop\job_market\Location_encoding.pkl", 'rb') as f:
    Location_encoding = pickle.load(f)
with open(r"C:\Users\manoj\Desktop\job_market\Role_encoding.pkl", 'rb') as f:
    Role_encoding = pickle.load(f)
Skills=['Technical Support',
       'Communication Support', 'Front Desk', 'Medical Support',
       'Java Development', 'Python Development', 'Full Stack JavaScript',
       'Web Development', 'Microsoft Stack', 'Angular Development',
       'Testing QA', 'Data Analytics', 'Design and UI/UX',
       'Administrative and Coordination', 'Sales and Business Development',
       'Team and Project Management', 'Healthcare and Medical',
       'Procurement and Inventory', 'Education and Training',
       'Engineering and Technical', 'Mobile App Development',
       'Legal and Compliance']

# Load Model
model = joblib.load(r"C:\Users\manoj\Desktop\job_market\xgb.pkl")  # Your Random Forest model

# Input DataFrame Columns
input_columns = ['Job Title', 'Job Experience Required', 'Role', 'Location','Skills'
       ]

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Salary Estimation", ["Home", "Project Overview", "Estimate Outcome"], 
        icons=['house', 'info-square-fill','stethoscope'], 
        menu_icon="cast", default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "black"},
            "icon": {"color": "white", "font-size": "18px"}, 
            "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "black"},
            "nav-link-selected": {"background-color": "blue"},
        }
    )

# Pages
if selected == 'Home':
    st.subheader(":green[Salary Estimation Project]",divider='blue')
    st.write("This project estimates salary outcomes based on job title, required experience, role, location, and associated skill sets.")
    colx, coly = st.columns([0.5,0.5])
    with colx:
        st.write("Using machine learning, specifically XGBoost models, we analyze job-related data—such as job title, experience, role, skills, and location—to estimate potential salary outcomes.")
    with coly:
        st.image("job_1.jpg")
    
    st.subheader(":red[Factors Considered in Estimation:]", divider='blue')
    colx, coly, colz = st.columns([0.2,0.6,0.2])
    with coly:
        st.image("job_2.jpg")
    
    st.write(":blue[Job Title:] Specifies the position or designation offered.")
    st.write(":blue[Experience Required:] Indicates how many years of work experience are necessary.")
    st.write(":blue[Skills:] Represents the core competencies needed for the job.")
    st.write(":blue[Role:] Denotes the function or responsibility area.")
    st.write(":blue[Location:] Impacts compensation based on geographic demand.")

elif selected == 'Project Overview':
    st.subheader(":green[Project Overview]", divider='blue')
    st.write("This dataset contains job information and their outcomes based on various factors collected over several years.")
    st.write(":blue[Dataset Sample:]")
    st.dataframe(df.head())

    st.write(f"Total Records: {df.shape[0]}, Features: {df.shape[1]}")
    colx, coly, colz = st.columns([0.2,0.4,0.2])
    with coly:
        st.image("job_3.jpg")
    
    st.subheader(":green[Machine Learning Modeling]", divider='blue')
    st.write("Trained an XGBoost regression model using key categorical features such as job title, role, location, skills, and experience.")

    st.write(":blue[Performance:]")
    st.write("- High Estimation accuracy on validation data")
    st.write("- Effectively handles complex patterns in categorical job market data")


else:
    st.subheader(":green[Estimation of salary]", divider='blue')
    st.write("Enter below details to get estimated salary outcome:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        job_title = st.selectbox("Select Job Title:", df['Job Title'].unique())
    
    with col2:
        job_experience = st.number_input("Enter Job Experience:", min_value=0, max_value=30, value=5)

    col4, col5 = st.columns(2)
    with col3:
        role = st.selectbox("Select Role:", df.Role.unique())
    with col4:
        location = st.selectbox("Select Location:", df.Location.unique())
    with col5:
        skill = st.selectbox("Select Skills:", Skills)
        input_skills = {s: 1 if s == skill else 0 for s in Skills}
        

# Create one-hot encoded symptom vector
        
    if st.button("Estimate", type='primary'):
        # Prepare Input Row
        input_data = {
            'Job Title':Job_Title_encoding[job_title], 'Job Experience Required':job_experience,'Role':Role_encoding[role], 'Location':Location_encoding[location], **input_skills
        }

# Create DataFrame from dictionary
        input_row = pd.DataFrame([input_data])
        st.write(":green[Given Input Data:]")
        st.markdown("<hr style='margin-top: 1px;'>", unsafe_allow_html=True)
        st.dataframe(input_row)


        # Estimation (no scaling needed!)
        Estimation = model.predict(input_row)[0]

        st.subheader(f":blue[Estimated min Salary:] {round(Estimation[0])*100000}")
        st.subheader(f":blue[Estimated max Salary:] {round(Estimation[1])*100000}")