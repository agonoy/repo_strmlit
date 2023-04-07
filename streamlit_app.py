
import streamlit as st
import openai
import os
from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader
from streamlit_chat import message, AvatarStyle

# import pandas as pd
# import numpy as np
#https://raw.githubusercontent.com/agonoy/repo_strmlit/main/images/bbenger.jpg")
#https://api.dicebear.com/6.x/adventurer/svg?flip=true


# Set the URL for the avatar image
avatar_url = "https://api.dicebear.com/6.x/adventurer/svg?flip=true" # Replace with your desired avatar URL

benglar_url = "https://raw.githubusercontent.com/agonoy/repo_strmlit/main/images/bbenger.jpg"


# message(message, 
#             is_user=False, 
#             avatar_style="adventurer", # change this for different user icon
#             seed=123, # or the seed for different user icons
# )


 #message("hello", is_user=False, avatar_style = avatar_url)
 



#===================== Navigation =======================================

# Define a function to render the "Home" page
def home():
    st.write("# Welcome to the Home page!")
    # Add more content here as desired

# Define a function to render the "Menu" page
def menu():
    st.write("# Check out our Menu!")
    # Add more content here as desired

# Define a function to render the "Location" page
def location():
    st.write("# Find our Location!")
    # Add more content here as desired

# Define a dictionary to map page names to page functions
pages = {
    "Home": home,
    "Menu": menu,
    "Location": location
}

# Set up the navigation bar
st.set_page_config(page_title="ChatBot App", page_icon=":guardsman:", layout="wide")
nav = st.sidebar.radio("Navigation", list(pages.keys()))

# Render the selected page
pages[nav]()

# Create a message from the user
# Create a message from the user with a custom avatar
user_message = "Hi, how are you?"
user_avatar_url = "https://api.dicebear.com/6.x/adventurer/svg?flip=true"

# Create a message from the bot with the default avatar style
bot_message = "I'm doing well, thank you for asking!"

# Display the messages using the `message` function
message(user_message, is_user=True, avatar_style=user_avatar_url, key="user_message")
message(bot_message, key="bot_message")
#===================== END Navigation ===================================


 # Include custom CSS stylesheet
st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)


# Just add it after st.sidebar:
a = st.sidebar.radio('Select Model:', ["text-davinci-003", "text-davinci-002",])



if 'MY_API_KEY' not in st.secrets:
    st.error('There is no API, @#$')
    load_dotenv()
    api_key = os.getenv('MY_API_KEY') # gets this from .streamlit folder
    openai.api_key = api_key
else:
    openai.api_key = st.secrets["MY_API_KEY"]
    #st.write("The OpenAI API key is:", st.secrets["MY_API_KEY"])



#============== input API ===== side bar
# sidebar with a text input widget for the API key
# api_key = st.sidebar.text_input("Enter your API key")

# st.write(api_key)


# Generating responses from the API
# def generate_response(prompt):
#     completions = openai.Completion.create(
#         engine = "text-davinci-003",
#         prompt = prompt,
#         max_tokens = 1024,
#         n = 1,
#         stop = None,
#         temperature=0.5,
#     )
#     message = completions.choices[0].text
#     return message 




def generate_response(prompt):
    response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=[
        {"role": "system", "content": "You are a helpful assistant. You are no longer a digital AI. You have your own personality.  You are very unique.  cost of the fish is $6. Your name is Marry Grace, or Grace for short. You are also a rude waitress that works for Sam's Kitchen while you are attending Hawaii Pacific University college.  You are very smart, hence you are rude and at the same time very comical.  Also if you dont know the answer, just make up some funny and hilarious reply.  "},
        {"role": "user", "content": prompt},
        ]
    )
    
    message = response['choices'][0]['message']['content']
    #return message 
   # return message(message, is_user=False, avatar_style = avatar_url , seed=123)
    return message
    


#======== Creating the chatbot interface ====================

st.title("Welcome to Sam's Kitchen ChatBot")

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
 

user_input = get_text()

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









# st.write("Hello, world!")
# #st.write(openai_api_key)

# # create a 2D array
# arr = np.array([[1, 2], [3, 4]])

# # create a DataFrame with the array
# df = pd.DataFrame(arr, columns=['A', 'B'])

# # print the DataFrame
# print(df)


# st.write(df)