#!/usr/bin/python3
"""
Define the user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Extends the BaseModel parent class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
