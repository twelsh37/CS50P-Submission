# -*- coding: utf-8 -*-
'''
DESCRIPTION:
This is the main file of our Application. From here we run our streamlit app, and from that we are able to launch the
 streamlit application

:Author: Tom
:Created: 21/06/2022
:Copyright: Tom Welsh - twelsh37@gmail.com
'''
# Our imports
import os
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import streamlit_authenticator as stauth
import plotly.express as px
from deta import Deta
from dotenv import load_dotenv
import openpyxl

#basic housekrrping for the App
st.set_page_config(page_title="Data Explorer", layout="wide")

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
        st.markdown('---')

    #--- Our SIDEBAR ---#
    st.sidebar.title('Options')

    # Functions
    # for each of the pages
    # Definitions for our selectbox in the sidebar
    def page_select():
        if not "7 Wondors Of The World" or "African Game Parks" or "Most Populous Cities In The World":
            st.subheader('Select a page from the drop select box in the sidebar')

    def page_7wonders():
        st.sidebar.header("7 Wonders of the Ancient World")

    def page_africanparks():
        st.sidebar.header("A Selection of African Wildlife Parks")

    def page_cities():
        st.sidebar.header("Top 100 Most Populous Cities")

    pages = {
        "Select Data To Be Displayed": page_select,
        "7 Wondors Of The World": page_7wonders,
        "African Game Parks": page_africanparks,
        "Most Populous Cities In The World": page_cities
    }

    selected_page = st.sidebar.selectbox("Select Page", pages.keys())
    pages[selected_page]()

    # Column setup
    col1, col2, col3 = st.columns(3)

    # Sidebar setup
    st.sidebar.title('Sidebar')
    upload_file = st.sidebar.file_uploader('Upload a file with latitude and longitude data')

    # Check if file has been uploaded
    if upload_file is not None:
        df_upload = pd.read_excel(upload_file)
        st.map(df_upload)

    # Select box actions
    if selected_page == "7 Wondors Of The World":
        with col1:
            df1 = pd.read_csv('7wonders.csv')
            st.title('The 7 Wonders Of The World')
            st.map(df1)
        with col2:
            st.title("Mapping Information")
            st.write(df1.head(7))
        with col3:
            st.title("Plotly interactive Chart")
            fig = px.scatter_mapbox(df1,
                                    lat='latitude',
                                    lon='longitude',
                                    # color='Maximum total people killed',
                                    # size='Maximum total people killed',
                                    color_continuous_scale=px.colors.cyclical.IceFire,
                                    size_max=20,
                                    width=1000,
                                    height=600,
                                    )
            # Set the center point of the map and the starting zoom
            fig.update_mapboxes(center=dict(lat=19, lon=45),
                                zoom=3,

                                )
            fig.update_traces(
                # This removed the colorbar
                marker_coloraxis=None
            )

            # Plot!
            st.plotly_chart(fig, use_container_width=True)
    elif selected_page == "African Game Parks":
        with col1:
            df2 = pd.read_csv('africanparks.csv')
            st.title('A Selection of African Gaame Parks')
            st.map(df2)
        with col2:
            st.title("Mapping Information")
            st.write(df2.head(7))
        with col3:
            st.title("Dataframe Info")
            st.write(df2.describe())
    elif selected_page == "Most Populous Cities In The World":
        with col1:
            df3 = pd.read_csv('worldcities.csv')
            st.title('100 Of The Worlds Most Populous Cities')
            st.map(df3)
        with col2:
            st.title("Mapping Information")
            st.write(df3.head(7))
        with col3:
            st.title("Dataframe Info")
            st.write(df3.describe())


    # STICK A LOGOUT BUTTON IN THE SIDEBR
    authenticator.logout("Logout", "sidebar")

# def interactive_plot():
#     col1, col2 = st.columns(2)
#
#     x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
#     y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)
#
#     plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
#     st.plotly_chart(plot, use_container_width=True)

#--- DATABASE HANDLING ---#
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
