import streamlit as st

# if 'slider' not in st.session_state:
#     st.session_state.slider = 25

# min_value  = st.slider("set min value ",0,50,25)
# st.session_state.slider = st.slider("Slider",min_value,100,st.session_state.slider)

# #In this code we use session state because by deafult it will not moved by min value 
# # as previously we used min value as defalut in parameter


if "checkbox" not in  st.session_state:
    st.session_state.checkbox = False

def toggleInput():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show input field",value= st.session_state.checkbox, on_change=toggleInput)

if st.session_state.checkbox:
    user_input = st.text_input("Enter something: ",value=st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get('user_input','')
st.write(f'User Input: {user_input}')