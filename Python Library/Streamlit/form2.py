import streamlit as st
from datetime import datetime

min_date = datetime(1990,1,1)
max_date = datetime.now()

st.title('User info form')

with st.form(key='user_info'):
    name = st.text_input('Enter your name: ')
    birthdate = st.date_input('Enter your birthdate:',min_value=min_date,max_value=max_date)

    if birthdate:
        age = max_date.year-birthdate.year
        if (birthdate.month > max_date.month) or( birthdate.month == max_date.month and  birthdate.day > max_date.day):
            age-=1
        st.write(f'your age is {age} years')

    submit_button = st.form_submit_button('Submit')
    if submit_button:
        if not name or not birthdate:
            st.warning('Please fill all details')
        else: 
            st.success(f'Thank you, {name}.Your age is {age}')
            st.balloons()
            