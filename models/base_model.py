#!/usr/bin/python3
"""
Define the BaseModel class
"""

import uuid
from datetime import datetime

class BaseModel:
    """ The base model to use to extend our other classes """

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Returns string representation of current object """
        return"[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute 'updated_at' with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__  of the instance """
        dict_ = self.__dict__
        dict_["__class__"] = self.__class__.__name__

        if "created_at" in dict_:
            dict_["created_at"] = dict_["created_at"].isoformat()
        if "updated_at" in dict_:
            dict_["updated_at"] = dict_["updated_at"].isoformat()

        return (dict_)
