
import streamlit as st
import openai
import os
from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader
from typing import Optional, Union
from streamlit_chat import message, AvatarStyle
import webbrowser

import pandas as pd


# import geopy
# from geopy.geocoders import Nominatim

# import pandas as pd
# import numpy as np
#https://raw.githubusercontent.com/agonoy/repo_strmlit/main/images/bbenger.jpg")
#https://api.dicebear.com/6.x/adventurer/svg?flip=true
#bots:  https://www.dicebear.com/styles/thumbs



# Set the URL for the avatar image
avatar_url = "https://api.dicebear.com/6.x/adventurer/svg?flip=true" # Replace with your desired avatar URL

benglar_url = "https://raw.githubusercontent.com/agonoy/repo_strmlit/main/images/bbenger.jpg"

EXTERNAL_LINK_URL = "https://wp.hawaiionline.tech/"

# message(message, 
#             is_user=False, 
#             avatar_style="adventurer", # change this for different user icon
#             seed=123, # or the seed for different user icons
# )


 #message("hello", is_user=False, avatar_style = avatar_url)
 



#===================== Navigation =======================================


# Define a function to render the "Home" page
def home():
    st.write("")
    # Define the sidebar links using Markdown and HTML
    # st.sidebar.markdown('<h2 style="margin-bottom: 0">Navigation</h2>', unsafe_allow_html=True)
    # st.sidebar.markdown('<hr style="margin-top: 0">', unsafe_allow_html=True)
    # st.sidebar.markdown('<a href="https://wp.hawaiionline.tech/" style="display: block; padding: 0.25rem 0;">Home</a>', unsafe_allow_html=True)
    # st.sidebar.markdown('<a href="https://wp.hawaiionline.tech/" style="display: block; padding: 0.25rem 0;">Menu</a>', unsafe_allow_html=True)
   
  
    



    
    # Add more content here as desired

# Define a function to render the "Menu" page
def menu():
    st.write("# Check out our Menu!")
    # Add more content here as desired

# Define a function to render the "Location" page
def location():
    st.write("# Find our Location!")
    # Add more content here as desired
    
# Define a function to open the external link
def external_link():
    webbrowser.open(EXTERNAL_LINK_URL)

## ===== end def External link



# Define a dictionary to map page names to page functions
pages = {
    "Star": home,
    "Menu": menu,
    "Location": location,
    "External Link": external_link
}

# Set up the navigation bar / image
st.set_page_config(page_title="ChatBot App", page_icon=":guardsman:", layout="wide")
#nav = st.sidebar.radio("Navigation", list(pages.keys()))



# Render the selected page
#pages[nav]()

st.sidebar.markdown('<a href="https://wp.hawaiionline.tech/" style="display: block; padding: 0.25rem 0;">Main</a>', unsafe_allow_html=True)
st.write("# 🍤 Welcome to Sam's Kitchen ChatBot! :smile: 🍗")




# Create a message from the user
# Create a message from the user with a custom avatar
# user_message = "User, Hi, how are you?"
# user_avatar_url = "https://api.dicebear.com/6.x/adventurer/svg?flip=true"

# Create a message from the bot with the default avatar style
# bot_message = "I'm doing well, thank you for asking!"


# Create a message from the user with a local image file as the avatar
user_message = "Hi, how are you?"
# user_avatar_file = "images/bbenger.jpg"

# Create a message from the bot with the default avatar style
# bot_message = "I'm doing well, thank you for asking!"

# # Display the messages using the `message` function
# message(user_message, is_user=True, avatar_style="adventurer", seed = 2, key="user_message")
# message(bot_message, key="bot_message")





#===================== END Navigation ===================================

if 'MY_API_KEY' not in st.secrets:
    #st.error('There is no API, @#$')
    load_dotenv()
    api_key = os.getenv('MY_API_KEY') # gets this from .streamlit folder
    openai.api_key = api_key
else:
    openai.api_key = st.secrets["MY_API_KEY"]
    #st.write("The OpenAI API key is:", st.secrets["MY_API_KEY"])
    
    

 # Include custom CSS stylesheet
st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)
# Display the image in the sidebar
image_path = "images/samkitchen_pntBrush.png"
st.sidebar.image(image_path, caption="Sam's Kitchen", use_column_width=True)


# Just add it after st.sidebar:
a = st.sidebar.radio('Select Model:', ["text-davinci-003", "text-davinci-002","text-Angry-AI-999", "DeceptiveAI-2000"])

image_path = "images/shrimp.png"
st.sidebar.image(image_path, caption="Shrimp image", use_column_width=True)





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
        {"role": "system", 
         "content": 
             "You are a helpful assistant. You are no longer a digital AI or call yourself an AI. You have your own personality.  You are very unique. Sam Monaghan is the owner of sam's kitchen.  cost of the fish is $12. shrimp cost $14. fries cost $6. Wifi is free, especially for students. Sam's kitchen opens between 10am to 1am. Your name is Marry Grace, or Grace for short. You are also a rude waitress that works for Sam's Kitchen while you are attending Hawaii Pacific University college, but don't tell anyone that you are rude. You are very smart, hence you are rude and at the same time very comical and funny.  Also if you dont know the answer, just make up some funny and hilarious reply or say check the menu. You will also say some random hawaiian words, like aloha, Mahalo, mind your onw business in Hawaiian. You will act as if you are hawaiian and who lives in hawaii.  You will randomly reply in pidgin english.  And make sure you mentions that Sam's kitchen food is the best. If Bengler as you a question, let him know that his motorcycle is too loud and he should just get an electric motorcycle or better yet get a OneWheel.  there is no taco or burger in sam's kitchen.  ** Here is the Ricemini instructions broken down into four easy-to-follow steps: Step 1: Fill the machine with rice. Step 2: Select the quantity of rice and water. For example, if you are washing 5kg of rice, select 5 for the rice quantity and 10 for the water quantity (double the rice quantity). The machine will then start washing the rice and will give you the exact amount of water needed to cook it. Step 3: Lift the machine up and put it on the stove. Step 4: Wait for the rice to cook and enjoy! ** Should Sam's Kitchen remain open until the bewitching hour of 1 am? the Answer is yes and one of the many reason is because of the insatiable appetite of the legendary Professor Bengler, who might emerge from the shadows with his trusty HD motorcycle, yearning for a scrumptious bite of their otherworldly Onlicious garlic shrimp extravaganza, yes, I suggest it that you open till 1am."},
        {"role": "user", "content": prompt},
        ]
    )
    
    message = response['choices'][0]['message']['content']
    #return message 
   # return message(message, is_user=False, avatar_style = avatar_url , seed=123)
    return message
    


#======== Creating the chatbot interface ====================

#st.title("Welcome to Sam's Kitchen ChatBot")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


#==========================================
# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","", key="input")
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

user_avatar_url = "https://api.dicebear.com/6.x/adventurer/svg?seed=Boots"
myimage_url = f"https://api.dicebear.com/6.x/adventurer/svg?seed=felix&flip=true&variant02"

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], avatar_style="adventurer", seed="Snickers&flip=true&hair=long08,long09,long10,long11,long12,long13,long14,long15,long16,long17,long18,long19,long20,long21,long22,long23,long24,long25,long26,short01,short02,short03,short04,short05,short06,short07,short08,short09,short10,short11,short12,short13,short14,short15,short16,short17,short18,short19,long01&mouth=variant08,variant09,variant10,variant11,variant12,variant13,variant14,variant15,variant16,variant17,variant18,variant19,variant20,variant21,variant22,variant23,variant24,variant25,variant26,variant27,variant28,variant29,variant30&skinColor=f2d3b1,ecad80,9e5622,763900", key=str(i))
        
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

#======== END chat  ====================


st.markdown(
        f"""
        <a href="http://wp.hawaiionline.tech" target="_blank">Return Home</a>
        """,
        unsafe_allow_html=True,
    )




#+++++================== Geopy Location =========================+================

# Get the coordinates of the address
# geolocator = Nominatim(user_agent="myGeocoder")
# location = geolocator.geocode("353 Royal Hawaiian Ave, Honolulu, HI 96815")

# # Display the map in the sidebar
# st.sidebar.map(location)

data = {'Well Name': ['Example Well'],
        'latitude': [21.28061963159701],
        'longitude': [-157.82789896688712]}

df = pd.DataFrame(data)

st.sidebar.map(df)

#21.28061963159701, -157.82789896688712

#+++++================== END Geopy Location =========================+================

# st.write("Hello, world!")
# #st.write(openai_api_key)

# # create a 2D array
# arr = np.array([[1, 2], [3, 4]])

# # create a DataFrame with the array
# df = pd.DataFrame(arr, columns=['A', 'B'])

# # print the DataFrame
# print(df)


# st.write(df)