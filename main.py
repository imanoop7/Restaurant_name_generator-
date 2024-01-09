import streamlit as st
import name_genrator


st.title('Resturant Name Genrator')


cuisine =st.sidebar.selectbox('Pick a Cuisine',('Indian','Italian','Mexican',"Arabic",'American','Japanese','Korean'))



if cuisine:
   response= name_genrator.genreate_resurant_name_and_items(cuisine)
   st.header(response['resturant_name'].strip())
   menu_items = response['menu_items'].strip().split(',')
   st.write("**Menu Items**")
   
   for item in menu_items:
       st.write('-\n',item)

