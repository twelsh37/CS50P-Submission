# -*- coding: utf-8 -*-
'''
Documentation: - Delete when complete
* Talk to 'Future You' readint the methods and classes 6/8 months from now.
* Future you has spent those months on 5/6 other projects and cant
remember any of this.
* Future you doesn't have time to spend a full day trying to 'get
into' the code in order to fix a bug / adapt a method.
* Be Generous to future you, that will be you some day.

DESCRIPTION:

Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

:Author: Tom
:Created: 17/07/2022
:Copyright: Tom Welsh - twelsh37@gmail.com
'''
import os
import streamlit as st
import streamlit_authenticator as stauth
import plotly.express as px
from deta import Deta
from dotenv import load_dotenv
import yaml

# basic housekrrping for the App
st.set_page_config(page_title="Data Explorer", page_icon="🌎", layout="wide", initial_sidebar_state="collapsed")

# Load our environment files
load_dotenv(".env")

# Our Project Keys
DETA_KEY = os.getenv("DETA_KEY")

# Our Mapbox Token
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")

# Give mapbox token to Plotly Express
px.set_mapbox_access_token(MAPBOX_TOKEN)

# Initialise with a project key
deta = Deta(DETA_KEY)

# Create database connection
db = deta.Base("users_db")


# Our Main function
def main():
    # --- USER AUTHENTICATION SECTION ---#
    # users = fetch_all_users()
    with open('config.yaml') as file:
        config = yaml.safe_load(file)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    # From Streamlit login form store our input in variables
    name, authentication_status, username = authenticator.login("Login", "main")

    # Hide hamburger and sidebar
    st.markdown("""
    <style>
     .e1fb0mya1 {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

    # If authentication fails reprompt for Username/password
    if authentication_status == False:
        st.error("Username/password is incorrect")

    # if just hits login ask them to login
    elif authentication_status == None:
        st.warning("Please enter your username and password")

    # if user is authenticated show the app
    elif authentication_status == True:
        st.title('Data Explorer')
        st.markdown('#### Description:')
        st.markdown('''
        This is my final project submission for Harvard Universitys CS50P.
        The application utilises an open-source application framework for building the web application.
        The application is frontended by a login page where only authorised users can gain access to the main application.
        The login page is back-ended to the [Deta Base NoSQL database](https://www.deta.sh/), which is used to store our user credentials.
        When the user gains access to the main application Area they are presented with an opening page displaying a stock ticker for user selectable instraments, Some metric boxes for the associated ticker symbols.
        There are then other selectable options available in the side bar that will allow the user to display different information.''')
        st.markdown(' ')
        st.markdown('### Examples of this kind of data are')
        st.markdown('''
        * 7 Wonders of The World
        * A selection of African Game Parks
        * The 100 most populous cities on Earth
                    ''')
        st.markdown(' ')
        st.markdown('Below is the data for the 7 wonders of the world which will be plotted on a digital map.')
        st.markdown('#### The 7 Wonders of the Ancient World')
        code1 = '''| Name                          | Country 	| Latitude              | Longitude          	|
|------------------------------	|---------	|--------------------	|--------------------	|
| Statue of Zeus at Olympia    	| Greece  	| 37.63819915960268  	| 21.63011753949122  	|
| Temple of Artemis at Ephesus 	| Turkey  	| 37.94967735447476  	| 27.363909843917902 	|
| Mausoleum at Halicarnassus   	| Turkey  	| 37.03803297044549  	| 27.424116399008735 	|
| Colossus of Rhodes           	| Turkey  	| 36.45107354911518  	| 28.2257819413324   	|
| Hanging Gardens of Babylon   	| Iraq    	| 36.57693767402696  	| 41.869210073371086 	|
| Great Pyramid of Giza        	| Egypt   	| 29.97942034949402  	| 31.134244814303447 	|
| Lighthouse of Alexandria     	| Egypt   	| 31.214081589823174 	| 29.8855234134948   	|'''
        st.code(code1, language='text/plain')
        st.markdown(
            'Source: https://blog.batchgeo.com/seven-wonders-of-the-world-more-like-46-wonders/ <Accessed 2022-06-08>')
        st.markdown(' ')
        st.markdown('### Design Decisions')
        st.markdown('''Having decided that my project was going to be an gui app of some kind i wanted to use a sutible medium to sisplay this on.
        A Gui type interface was my first choice.''')
        st.markdown('I considered the following four libraries for the GUI.')
        st.markdown('''
        * Kivy - https://github.com/kivy/kivy - I discarded this as it seemed more focused on multi-touch devices.
        * Tkinter - https://docs.python.org/3/library/tkinter.html - The grandad of the Python GUI frameworks. This turned out to be hard to test with pytest so I discounted it.
        * Dash/Plotly - https://plotly.com/dash/ - A modern day gui tool used to build web based applications and dashboards. Integrates well with plotly.I have used it before so discounted as i wanted to learn a new library
        * Streamlit - https://streamlit.io - Open source application Framework for developing web apps.

        **Decision** - Select Streamlit to create our final project.
        ''')
        st.subheader('Project files')
        st.markdown('This project was created using the following files:')
        code = '''
  project
    ├── .env                                        # Environment files
    ├── .streamlit                                  # Streamlit configuration files
    │   └── config.toml                             # Streamlit configuration file
    ├── 7wonders.csv                                # Data file for the 7 Wonders of the World
    ├── README.md                                   # Readme file
    ├── africanparks.csv                            # Data file for the African Game Parks
    ├── config.yaml                                 # Database user configuration file 
    ├── pages                                       # Page files
    │   ├── 01_1️⃣_African_Parks.py                  # Page 1                  
    │   ├── 02_2️⃣_Seven_Wonders_of_the_World.py     # Page 2
    │   ├── 03_3️⃣_stocks.py                         # Page 3
    │   └── 04_4️⃣_World_Cities.py                   # Page 4
    ├── project.py                                  # Main project file
    ├── requirements.txt                            # Requirements file
    ├── test_project.py                             # Test project file                             
    └── worldcities.csv                             # Data file for the World Cities
            '''
        st.code(code, language='text')

    # STICK A LOGOUT BUTTON IN THE SIDEBR
    authenticator.logout("Logout", "sidebar")


# --- DATABASE HANDLING ---#
# Lets just CRUD it up
# Create our user
def create_user(username, name, password):
    # Returns the user on a successful user creation, otherwise raises an error
    return db.put({"key": username, "name": name, "password": password})


# Read our user info
def read_user(username):
    # Returns our user info
    return db.get(username)


# Update our user
def update_user(updates, username):
    # Update user details
    return db.update(updates, username)


# Delete our user
def del_user(username):
    # Deletes a user
    return db.delete(username)


def fetch_all_users():
    # returns all our users in the db
    res = db.fetch()
    return res.items


if __name__ == '__main__':
    main()
