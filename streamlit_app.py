import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('spinach & rocket smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# lets put a pick list here so they can pick the fruit they want to include
streamlit.multiselect ("pick some fruits:",list(my_fruit_list.index))

#display the table on page
streamlit.dataframe(my_fruit_list)

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# lets put a pick list here so they can pick the fruit they want to include
streamlit.multiselect ("pick some fruits:",list(my_fruit_list.index))

#display the table on page
streamlit.dataframe(my_fruit_list)



# lets put a pick list here so they can pick the fruit they want to include
streamlit.multiselect ("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])

#display the table on page
streamlit.dataframe(my_fruit_list)

# lets put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect ("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on page
streamlit.dataframe(fruits_to_show)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response) 

streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
