
import streamlit as st
import openai
import os
from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader
from streamlit_chat import message

import pandas as pd
import numpy as np

# Just add it after st.sidebar:
a = st.sidebar.radio('Select Model:', ["text-davinci-003", "text-davinci-002",])


#============== input API ===== side bar
# sidebar with a text input widget for the API key
api_key = st.sidebar.text_input("Enter your API key")

st.write(api_key)



#MY_API_KEY  .. NOTE this will work in streamlit website by adding the API KEY
#my_api_key = os.environ["MY_API_KEY"]

openai.api_key = st.secrets["MY-API_KEY"]
# Now you can use the API key in your Python code
print(f"My API key is {my_api_key}")

st.write(my_api_key)

# Generating responses from the API
def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message 


#======== Creating the chatbot interface ====================

st.title("chatBot : Streamlit + openAI")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


#==========================================
# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text

#==========================================
# If user_input is not empty, we will generate a response using the generate_response function and store it in a variable called output. We will also append the user's input and the generated response to the past and generated lists, respectively, to keep track of the chat history.
# user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

#========  ====================
# Finally, we will display the chat history by iterating through the generated and past lists and using the message function from the streamlit_chat library to display each message.

if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


#======== END chat  ====================

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