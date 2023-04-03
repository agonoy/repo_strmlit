
import streamlit as st

import os
from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader


api_key2 = os.environ.get("NAME_API")

#load_dotenv()
#openai_api_key = os.getenv('OPENAI_API_KEY')

openai_api_key = os.getenv('NAME_API')

st.write("Hello, world!")
#st.write(openai_api_key)

import streamlit as st
import os

if 'env' not in st.secrets:
    st.error('No secrets were found.')
else:
    secrets = st.secrets['env']
    api_key = secrets['NAME_API']

st.write(openai_api_key)
st.write(api_key2)