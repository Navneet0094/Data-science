import streamlit as st

# sidebar layout
st.sidebar.title('This is a sidebar')
st.sidebar.write('You can place elements here')
sidebar_input = st.sidebar.text_input('You can enter here something')

tab1,tab2,tab3 = st.tabs(['Tab1','Tab2','Tab3'])

with tab1:
    st.write('You are in tab 1')
    col1 ,col2,col3 = st.columns(3)
    with col1:
        st.header('Column 1')
        st.write('Content for col1')
    with col2:
        st.header('Column 2')
        st.write('Content for col2')
    with col3:
        st.header('Column 3')
        st.write('Content for col3')


with tab2:
    st.write('You are in tab 2')

with tab3:
    st.write('You are in tab 3')

# CONTAINER 
with st.container(border=True):
    st.write('This is written inside container')
    st.write('You can think it as grouping of elements ')
    st.write('Containers help to manage sections of page')

# Empty placeholder
placeholder = st.empty()
placeholder.write('This is empty placeholder, useful for dynamic content')

if st.button('Update Placeholder'):
    placeholder.write('Placeholder is updated')

#expander

with st.expander("Expand for more details"):
    st.write('You can use expander to keep your ui clean')
    st.write('additional info is hidden bydefault')
 
# Popover (Tooltip)

with st.popover('Setting'):
    st.checkbox('completed')

st.write('Hover On this for a tooltip')
st.button('Button with tooltip',help='this is tooltop or popover on hover')
# sidebar input handeling
if sidebar_input:
    st.write(f'You entered in the sidebar: {sidebar_input}')
  