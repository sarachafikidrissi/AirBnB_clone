#!/usr/bin/python3
"""This is FileStorage Module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This is FileStorage Class
        used to serialize and deserialize objects onto and from files
    """
    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        pass

    def all(self):
        """returns the dictionary __objectss
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objectss the obj with key <obj class name>.id
        Attributes:
            obj (Python Object): The object to set
        """
        dictionary = obj.to_dict()
        key = "{}.{}".format(dictionary['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objectss to the JSON file (path: __file_path)
        """
        dictionary = dict()
        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesnt
        exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for k, v in json_load.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            pass
