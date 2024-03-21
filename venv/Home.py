import streamlit as st
import pandas

st.set_page_config(layout="wide")

cols1, empty_col, cols2 = st.columns([1.8, 0.2, 1.8])

with cols1:
    st.image("../images/photo.JPG")

with cols2:
    st.title("Lulu Xu")
    content = """
    Hi there, My name is Lulu, I am a Python Programmer, teacher, and a graduate student at Northeastern University, 
    majored in Computer Science. I'm open to SDE internship opportunitys.
    """
    st.write(content)

content2 = '''
Here are some of the apps that I have built.
Feel free to contact me!
'''
st.write(content2)

cols3, empty_cols, cols4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with cols3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("../images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with cols4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("../images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
