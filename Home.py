import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2=st.columns(2)

with col1:
    st.image("images/pfphoto.png", width=400)
    st.write("EMAIL: mondalsayandeep2004@gmail.com")
    st.write("PHONE NO: +9123729104")

with col2:
    st.title("Sayandeep Mondal")
    content="""Hi, I am Sayandeep. I am an aspiring Data Scientist and Machine Learning enthusiast, 
    currently pursuing B.Tech in Computer Science and Technology from Narula Institute of Technology.  
    My passion lies in transforming complex data into meaningful insights and leveraging machine 
    learning algorithms to solve real-world problems. My goal is to further develop my skills in 
    data science and machine learning, and to apply these skills in a dynamic and challenging environment.
    I am eager to contribute to innovative projects and collaborate with professionals who share my 
    passion for data-driven solutions."""
    st.info(content)

content2="Below you can find some of the apps I have built in Python. Do check them out and feel free to contact me!!"
st.info(content2)

col3, empty_col, col4=st.columns([2, 0.5, 2])

df=pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")