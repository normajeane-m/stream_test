import streamlit as st

st.title('Robotics Class(2024.05.23)')

# Using the "with" syntax
with st.form(key='my_form'):
	text_input = st.text_input(label='조 번호')
	genre = st.radio("Success",
	    [":rainbow[Success]", "***Still...***", "Problem :movie_camera:"],
	    captions = ["goooood", "Wait....", "Help!!"])
	
	submit_button = st.form_submit_button(label='Submit')
