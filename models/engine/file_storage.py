#!/usr/bin/python3
"""
Module for FileStorage class.
"""


import datetime
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:

    """
    Serializes instances to a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): dictionary to store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj


    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {
                key: obj.to_dict(
                ) for key, obj in self.__objects.items()
                }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
