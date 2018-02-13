#!/usr/bin/python3
"""
Define the User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Extends the 'BaseModel' parent class to create a 'User' class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
