#!/usr/bin/python3
"""
Define the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Extends the 'BaseModel' parent class to create a 'Review' class """

    place_id = ""
    user_id = ""
    text = ""
