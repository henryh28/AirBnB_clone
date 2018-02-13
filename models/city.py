#!/usr/bin/python3
"""
Define the City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Extends the 'BaseModel' parent class to create a 'City' class """

    state_id = ""
    name = ""
