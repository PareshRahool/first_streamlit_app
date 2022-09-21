import streamlit
import pandas
from urllib.error import URLError
import snowflake.connector
import requests

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
 
my_fruit_list=my_fruit_list.set_index('Fruit')


#Let's put a pick list here so they can pick the fruit they want to include

# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# #display the table on the page
# streamlit.dataframe(my_fruit_list)



fruit_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show= my_fruit_list.loc[fruit_selected]
#display the table on the page
streamlit.dataframe(fruit_to_show)

#New Section to display fruitvice api response
#import requests

streamlit.header("Fruitvice Fruit Advice!")
fruit_choice=streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered',fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json()) #just write the data to the screen

#Take the json version of the response and normalize it
fruitvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruitvice_normalized)

#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

#streamlit.text("What fruit would you like to add?")
add_my_fruit=streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ',add_my_fruit)
