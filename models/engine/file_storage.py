#!/usr/bin/python3
"""
Serialize/deserialize objects to/from JSON files
"""
import json
from models.base_model import BaseModel
from collections import namedtuple


class FileStorage():
    """ Serializes/deserializes objects """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns a dictionary __objects """
        return (FileStorage.__objects)

    def new(self, obj):
        """ Sets __objects with key <obj class name>.id """

        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ Serializes __objects to JSON file using path '__file_path' """

        save_dict = {}
        with open(self.__file_path, 'w', encoding='utf-8') as fs:
            for key, value in self.__objects.items():
                save_dict[key] = value.to_dict()

            json.dump(save_dict, fs)

    def reload(self):
        """ Deserializes JSON file to __objects only if JSON file exists """

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fs:
                revived = json.load(fs)

            for key, value in revived.items():
                if "__class__" in value and revived[key][
                        "__class__"] == "BaseModel":
                    FileStorage.__objects[key] = BaseModel(**value)
        except:
            pass