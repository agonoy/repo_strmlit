
import streamlit as st

import os
from dotenv import load_dotenv


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')



st.write("Hello, world!")
st.write(openai_api_key)
