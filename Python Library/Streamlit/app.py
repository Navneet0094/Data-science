import streamlit as st
import os

st.write('hello world')

# print('run')
# pressed = st.button('Press me')
# print(pressed)
# pressed1 = st.button('mujhe dabao')
# print(pressed1)


# text elements
st.title('this is title')
st.header('header')
st.subheader('subheader')
st.caption('small text')
st.markdown('this is a markdown')

code_example ="""
def greet(name):
    print('hello',name) 
"""
st.code(code_example,language='python')
st.divider()

#images
st.image(os.path.join(os.getcwd(),"static","images.jpeg") ,width=100,caption='demo')


