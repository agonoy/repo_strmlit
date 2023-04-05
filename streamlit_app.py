
import streamlit as st

import os
from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader


import pandas as pd
import numpy as np

# Just add it after st.sidebar:
a = st.sidebar.radio('Select Model:', ["text-davinci-003", "text-davinci-002",])


#============== input API ===== side bar
# sidebar with a text input widget for the API key
api_key = st.sidebar.text_input("Enter your API key")

st.write(api_key)

# Read the value of the environment variable
#api_key = os.getenv('API_NAME')

my_api_key = os.environ["MY_API_KEY"]

# Now you can use the API key in your Python code
print(f"My API key is {my_api_key}")


#api_key2 = os.environ["MY_API_KEY"]

#load_dotenv()
#openai_api_key = os.getenv('OPENAI_API_KEY')

#openai_api_key = os.getenv('NAME_API')

st.write("Hello, world!")
#st.write(openai_api_key)


if 'env' not in st.secrets:
    st.error('No secrets were found.')
else:
    #secrets = st.secrets['env']
    api_key = st.secrets['NAME_API']

#st.write(openai_api_key)
st.write(api_key)


# create a 2D array
arr = np.array([[1, 2], [3, 4]])

# create a DataFrame with the array
df = pd.DataFrame(arr, columns=['A', 'B'])

# print the DataFrame
print(df)


st.write(df)