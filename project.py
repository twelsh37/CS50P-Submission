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
:Created: 21/06/2022
:Copyright: Tom Welsh - twelsh37@gmail.com
'''
import os
import streamlit as st
import streamlit.components.v1 as components
import streamlit_authenticator as stauth
from deta import Deta
from dotenv import load_dotenv
#import database as db


st.set_page_config(page_title="Data Explorer", layout="wide")

# Load our environment files
load_dotenv(".env")

# Our Project Keys
DETA_KEY = os.getenv("DETA_KEY")

# Our Mapbox Token
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")

# Initialise with a project key
deta = Deta(DETA_KEY)

# Create database connection
db = deta.Base("users_db")

# Our Main function
def main():
    # --- USER AUTHENTICATION ---
    users = fetch_all_users()

    usernames = [user["key"] for user in users]
    names = [user["name"] for user in users]
    hashed_passwords = [user["password"] for user in users]

    # handle Authentication, cookie name, random key and cookie expiry time in days.
    # If you dont want passwordless reauthentication set it to 0 which will force you to login each time
    authenticator = stauth.Authenticate(
        names,
        usernames,
        hashed_passwords,
        "Data Explorer",
        "abcdef",
        cookie_expiry_days=0,
    )

    # From Streamlit login form store our input in variables
    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        st.header('Data Explorer')
        st.subheader('Lets play with some data')
        st.markdown('---')

    #--- SIDEBAR ---#
    authenticator.logout("Logout", "sidebar")

    st.sidebar.header('Options')


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
