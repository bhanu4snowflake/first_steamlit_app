 
import streamlit
import pandas
import requests
import snowflake.connector
#from urllib.error import URLError

streamlit.header('🥣 Breakfast favourites')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

       streamlit.text_input('What fruit would you like information about?')
