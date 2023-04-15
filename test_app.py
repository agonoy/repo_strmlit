import requests
import streamlit as st
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
css_path = os.path.join(dir_path, "style.css")


# # ---- LOAD ASSETS ----
# lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        


def main():
    st.set_page_config(page_title="Welcome to Sam's Kitchen ChatBot", layout="wide")
    st.title("Welcome to Sam's Kitchen ChatBot :wave:")
    
    
    
    
    
    
    
    
    
# Define the pages
def home():
    
    # Load the CSS file ( this might not be working)
    st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)
    
    #this works. . .
    local_css("style.css")
    

        # Add content for the Home page here
        #st.write("Welcome to Sam's Kitchen!")
    with st.container():
        # Define the two columns
        col1, col2 = st.columns([4, 4])
        # Add an image to the first column
        with col1:
            st.markdown('<div class="image-column">', unsafe_allow_html=True)
            st.image("images/samkitchen_pntBrush.png", width=300, output_format="PNG")
            st.markdown('</div>', unsafe_allow_html=True)

        # Add the chatbot to the second column
        with col2:
            st.subheader('Aloha! I am your Waitress :wave:')
            #st.header("Sam's Kitchen Chatbot")
            #st.write("Welcome to the chatbot!")
            
    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    #https://formsubmit.co/?utm_source=formsubmit.co&utm_medium=site%20link&utm_campaign=submission%20page
        contact_form = """
        <form action="https://formsubmit.co/bagonoy@hawaii.edu" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

def menu():
    # Add content for the Menu page here
    st.write("Our Menu")

def location():
    # Add content for the Location page here
    st.write("Our Location")


if __name__ == "__main__":
    main()
    home()
  
  




#------------- STARTS:   3 Columns w/ inside columns --------------------------------
# creates 3 columns.
# - 1 column will have 3 rows and 3 columns 
# - 2 column will have just one column 
# - 3 column will have 2 rows only 

# Create a container
container = st.container()

# Create 3 columns in the container with the middle column twice as wide
col1, col2, col3 = container.columns([1, 2, 1])

# Display 9 placeholders in the first column as a 3x3 grid
with col1.container():
    row1 = col1.columns(3)
    row2 = col1.columns(3)
    row3 = col1.columns(3)

    for i in range(3):
        row1[i].image("https://via.placeholder.com/200", use_column_width=True, caption=f"Placeholder image {i+1}")
        row2[i].image("https://via.placeholder.com/200", use_column_width=True, caption=f"Placeholder image {i+4}")
        row3[i].image("https://via.placeholder.com/200", use_column_width=True, caption=f"Placeholder image {i+7}")

# Display 2 placeholders in the third column
with col3.container():
    st.image("https://via.placeholder.com/200", use_column_width=True, caption="Placeholder image 10")
    st.image("https://via.placeholder.com/200", use_column_width=True, caption="Placeholder image 11")

# Run the Streamlit app
# if __name__ == "__main__":
#     st.set_page_config(page_title="Image Grid", layout="wide")
#     st.title("Image Grid")


#----------





# # Define the navigation bar
# nav = ["Home", "Menu", "Location"]
# page = st.sidebar.selectbox("Select a page", nav)

# #Display the selected page with the appropriate content
# if page == "Home":
#     home()
# elif page == "Menu":
#     menu()
# elif page == "Location":
#     location()




