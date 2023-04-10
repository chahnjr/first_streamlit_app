import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

def get_fruit_load_list():
   with my_cnx.cursor() as my_cur
        my_cur.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()
   
#find application @ https://share.streamlit.io/
streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(fruits_to_show)

streamlit.header('FruityVice Fruit Advice')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
   else:
      back_from_funtion = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_funtion)

except URLError as e:
   streamlit.error()
  
streamlit.stop()

streamlit.header("The fruit load list contains:")

if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
# add_my_fruit = streamlit.text_input('What fruit would you like to add?')

my_cur = my_cnx.cursor()


fruit_choice = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
                
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")                
