
#!/usr/bin/python3
"""
Define the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ The base model to use to extend our other classes """

    def __init__(self, *args, **kwargs):
        """ Constructor method """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key is 'created_at' or key is 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """ Returns string representation of current object """
        return"[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                    self.__dict__)

    def save(self):
        """ Updates the attribute 'updated_at' with the current datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary of the current instance """
        dict_ = self.__dict__
        dict_["__class__"] = self.__class__.__name__

        if "created_at" in dict_:
            if type(dict_["created_at"]) is str:
                dict_["created_at"] = datetime.strptime(dict_[
                    "created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            dict_["created_at"] = dict_["created_at"].isoformat()
        if "updated_at" in dict_:
            if type(dict_["updated_at"]) is str:
                dict_["updated_at"] = datetime.strptime(dict_[
                    "updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

            dict_["updated_at"] = dict_["updated_at"].isoformat()

        return (dict_)
