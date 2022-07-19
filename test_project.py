# -*- coding: utf-8 -*-
'''
DESCRIPTION:
Test suitefor project.py

This file tests the fumctions from project.py

:Author: Tom
:Created: 22/06/2022
:Copyright: Tom Welsh - twelsh37@gmail.com
'''

import pytest
from project import create_user
from project import read_user
from project import update_user
from project import del_user
from project import fetch_all_users


# Catch TypeError
def test_create_user_typeerror():
    with pytest.raises(TypeError):
        create_user(132)


# Catch TypeError
def test_create_user_nameerror():
    with pytest.raises(NameError):
        create_user(tom)


def test_create_user():
    assert create_user('atest', 'Test User', 'deleteme')


def test_read_user_typeerror():
    with pytest.raises(TypeError):
        read_user(132)


def test_read_user_nameeerror():
    with pytest.raises(NameError):
        read_user(tom)


def test_read_user():
    assert read_user('atest')

def test_del_user_typeerror():
    with pytest.raises(TypeError):
        del_user(132)


def test_del_user_nameeerror():
    with pytest.raises(NameError):
        del_user(tom)


def test_del_user():
    assert del_user('atest') == None


def test_fetch_all_users_typeerror():
    with pytest.raises(TypeError):
        fetch_all_users(132)


def test_fetch_all_users_nameeerror():
    with pytest.raises(NameError):
        fetch_all_users(tom)


def test_fetch_all_users():
    assert fetch_all_users()
