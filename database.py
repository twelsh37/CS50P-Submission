# -*- coding: utf-8 -*-
"""
:Author: 'twelsh'
:Created: 18/06/2022
:Copyright: Tom Welsh - twelsh37@gmail.com
"""


from deta import Deta
import os
from dotenv import load_dotenv

load_dotenv(".env")

# Our Project Keys
DETA_KEY = os.getenv("DETA_KEY")
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")

# Initialise with a project key
deta = Deta(DETA_KEY)

# Create database connection
db = deta.Base("users_db")


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
