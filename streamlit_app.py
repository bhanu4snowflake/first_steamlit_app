 
import streamlit
import pandas
import requests
import snowflake.connector


streamlit.header('🥣 Breakfast favourites')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruit_choice=streamlit.text('What fruit would you like information about?')

