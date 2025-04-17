import streamlit as st
st.title('Counter example for immediate rerun')

if 'count' not in st.session_state:
    st.session_state.count = 0 

def increment_and_rerun():
    st.session_state.count+=1
    st.rerun()
st.write(f'Current count: {st.session_state.count}')

if st.button('Increment and update immediately'):
    increment_and_rerun()
