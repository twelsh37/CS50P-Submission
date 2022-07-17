# -*- coding: utf-8 -*-
'''
DESCRIPTION:
This is the main file of our Application. From here we run our streamlit app, and from that we are able to launch the
 streamlit application
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

    elif authentication_status == None:
        st.warning("Please enter your username and password")

    elif authentication_status == True:
        st.title('Data Explorer')
        st.markdown('---')

    #---SIDEBAR ---#
    st.sidebar.title('Maps')

    # Functions
    # for each of the pages
    # Definitions for our selectbox in the sidebar

    def page_7wonders():
        #st.sidebar.header("7 Wonders of the Ancient World")
        pass

    def page_africanparks():
        #st.sidebar.header("A Selection of African Wildlife Parks")
        pass

    def page_cities():
        #st.sidebar.header("Top 100 Most Populous Cities")
        pass

    def page_upload():
        #st.sidebar.header("Top 100 Most Populous Cities")
        pass

    pages = {
        "7 Wonders Of The World": page_7wonders,
        "African Game Parks": page_africanparks,
        "Most Populous Cities In The World": page_cities,
        "Uploaded Files": page_upload
    }

    # Selectbox for our sidebar
    selected_page = st.sidebar.selectbox("Select Page", pages.keys())
    pages[selected_page]()

    # Column setup
    col1, col2 = st.columns(2)

    # Sidebar setup
    st.sidebar.title('File Upload')
    upload_file = st.sidebar.file_uploader('Upload a file containing latitude and longitude data', type = ['xlsx'])
    if upload_file is not None:
        df_upload = pd.read_excel(upload_file)
        st.map(df_upload)


    # Select box actions
    if selected_page == "7 Wonders Of The World":
        with col1:
            df1 = pd.read_csv('7wonders.csv')
            st.header("7 Wonders Of The World")
            fig = px.scatter_mapbox(df1,
                                    lat='latitude',
                                    lon='longitude',
                                    color = df1['name'],
                                    size_max=20,
                                    width=800,
                                    height=600,
                                    custom_data=[df1['name']]
                                    )
            # Set the center point of the map and the starting zoom
            fig.update_mapboxes(center=dict(lat=35, lon=33),
                                zoom=3.5,
                                )
            fig.update_layout(showlegend=False)
            fig.update_traces(
                # This removed the colorbar
                marker_coloraxis=None,
                hovertemplate='<B>Name: </B>'
            )

            # Plot!
            st.plotly_chart(fig, use_container_width=True, width=800, height=600)
        with col2:
            st.header("Mapping Information")
            st.dataframe(df1)

    elif selected_page == "African Game Parks":
        with col1:
            df2 = pd.read_csv('africanparks.csv')
            st.header("A Selection of African Game Parks")
            fig = px.scatter_mapbox(df2,
                                    lat='latitude',
                                    lon='longitude',
                                    color = df2['name'],
                                    size_max=20,
                                    width=800,
                                    height=600,
                                    custom_data = [df2['name']]
                                    )
            # Set the center point of the map and the starting zoom
            fig.update_mapboxes(center=dict(lat=4, lon=24),
                                zoom=1.75,
                                )
            fig.update_layout(showlegend=False)
            fig.update_traces(
                # This removed the colorbar
                marker_coloraxis=None,
                hovertemplate = '<B>Name: </B>'
            )
            # Plot!
            st.plotly_chart(fig, use_container_width=True, width=800, height=600)
        with col2:
            st.title("Mapping Information")
            st.write(df2.head(7))


    elif selected_page == "Most Populous Cities In The World":
        with col1:
            df3 = pd.read_csv('worldcities.csv')
            st.header("Most Populous Cities In The World")
            fig = px.scatter_mapbox(df3,
                                    lat='latitude',
                                    lon='longitude',
                                    color = df3['name'],
                                    size_max=20,
                                    width=800,
                                    height=600,
                                    custom_data=[df3['name']]
                                    )
            # Set the center point of the map and the starting zoom
            fig.update_mapboxes(center=dict(lat=24, lon=0),
                                zoom=0.2,
                                )
            fig.update_layout(showlegend=False)
            fig.update_traces(
                # This removed the colorbar
                marker_coloraxis=None,
                hovertemplate='<B>Name: </B>'
            )

            # Plot!
            st.plotly_chart(fig, use_container_width=True, width=800, height=600)
        with col2:
            st.title("Mapping Information")
            st.write(df3.head(7))


    elif (selected_page == "Uploaded File") and (upload_file is not None):
        with col1:
            df4 = pd.read_excel(df_upload)
            st.header("Drag and drop file")
            fig = px.scatter_mapbox(df4,
                                    lat='latitude',
                                    lon='longitude',
                                    color = df4['name'],
                                    size_max=20,
                                    width=800,
                                    height=600,
                                    custom_data=[df4['name']]
                                    )
            # Set the center point of the map and the starting zoom
            fig.update_mapboxes(center=dict(lat=24, lon=0),
                                zoom=0.2,
                                )
            fig.update_layout(showlegend=False)
            fig.update_traces(
                # This removed the colorbar
                marker_coloraxis=None,
                hovertemplate='<B>Name: </B>'
            )

            # Plot!
            st.plotly_chart(fig, use_container_width=True, width=800, height=600)
        with col2:
            st.title("Mapping Information")
            st.write(df4.head(7))


    # STICK A LOGOUT BUTTON IN THE SIDEBR
    authenticator.logout("Logout", "sidebar")

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

def hide_dataframe_row_index():
    hide_dataframe_row_index = """
    <style>
    .row_heading.level0 {display:none}
    .blank {display:none}
    </style>
    """
    return hide_dataframe_row_index


if __name__ == '__main__':
    main()