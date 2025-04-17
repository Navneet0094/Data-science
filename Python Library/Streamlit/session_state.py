import streamlit as st

# counter = 0 
# st.write(f'Counter value: {counter}')

# if st.button('Increment counter'):
#     counter+=1
#     st.write(f'Counter incremented to: {counter}')
# else:
#     st.write(f'Counter stays at: {counter}')

if 'counter' not in st.session_state:
    st.session_state.counter = 0
if st.button('Increment counter'):
    st.session_state.counter+=1
    st.write(f'Counter incremented to: {st.session_state.counter}')
if st.button('Reset'):
    st.session_state.counter = 0


st.write(f'Counter value: {st.session_state.counter}')
