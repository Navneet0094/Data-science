import streamlit as st
from datetime import datetime

st.title('User Info')
form_values = {
    'name': None,
    'height': None,
    'gender': None,
    'dob': None
}
min_date = datetime(1990,1,1)
max_date = datetime.now()

with st.form(key='sample_form'):
    form_values['name'] = st.text_input('Enter your name: ')
    form_values['height'] = st.number_input('Enter Your height: ')
    form_values['gender'] = st.selectbox('Gender',['Male','Female'])
    form_values['dob'] = st.date_input('Enter your dob: ',max_value=max_date,min_value=min_date)

    submit_button = st.form_submit_button()
    if submit_button:
        if not all(form_values.values()):
            st.warning('Please fill all details')
        else: 
            st.balloons()
            st.write('###info')
            for (key,value) in form_values.items():
                st.write(f"{key}:{value}")