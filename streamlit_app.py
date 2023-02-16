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
my_fruit_list = my_fruit_list.set_index('fruit')


# lets put a pick list here so they can pick the fruit they want to include
streamlit.multiselect ("pick some fruits:",list(my_fruit_list.index))

#display the table on page
streamlit.dataframe(my_fruit_list)
