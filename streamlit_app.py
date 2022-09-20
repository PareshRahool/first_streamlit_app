import streamlit
import pandas


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
import requests

streamlit.header("Fruitvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #just write the data to the screen

#Take the json version of the response and normalize it
fruitvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruitvice_normalized)

