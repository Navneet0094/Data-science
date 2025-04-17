import streamlit as st
# import time

# @st.cache_data(ttl=60) #cache this data for 60 sec
# def fetch_data():
#     #simulate a slow data fetching process
#     time.sleep(3) # delays to mimic an api call
#     return {'data':"this is cached data!"}
# st.write('fetching data ')
# data = fetch_data()
# st.write(data) 

file_path = 'example.txt'
@st.cache_resource

def get_file_handeler():
    #open file in append mode,which creates file if doesn't exist
    file = open(file_path,"a+")
    return file
# use cached file handler 
file_handler = get_file_handeler()
# write to file using cache handler

if st.button('Write to file'):
    file_handler.write('New line of text in example\n')
    file_handler.flush()#ensure content is written immediately
    st.success('write a new line to file')

# read and display file contents
if st.button('Read file'):
    file_handler.seek(0) # move to beginning of file
    content  = file_handler.read()
    st.text(content)

# always make sure to close file when done(useful for resource cleanup)
st.button('Close',on_click=file_handler)