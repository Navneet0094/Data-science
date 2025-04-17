import streamlit as st

st.title('My awesome app')

@st.fragment()
def toggle_and_text():
    cols= st.columns(2)
    cols[0].toggle('toggle')
    cols[1].text_area('Enter text')

@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0] = st.checkbox('Filter')
    new_cols[1] = st.file_uploader('Upload Image')
    new_cols[2] = st.selectbox('Choose Option',['opt1','opt2','opt3'])
    new_cols[3] = st.slider('Select value',0,100,50)
    new_cols[3] = st.text_input('Enter text')

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox('Select',[1,2,3],None)
cols[1].button('Update')

filter_and_file()