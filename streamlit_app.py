  
import streamlit
import pandas
import requests
import snowflake.connector
#from urllib.error import URLError

streamlit.header("Fruityvice Fruit Advice!")
#try:  
     fruit_choice = streamlit.text_input('What fruit would you like information about?')
#if fruit_choice:
    #   streamlit.error("Please select a fruit to get information.")
#else:
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       streamlit.dataframe(fruityvice_normalized)

#except URLError as e:
 #  streamlit.error()


