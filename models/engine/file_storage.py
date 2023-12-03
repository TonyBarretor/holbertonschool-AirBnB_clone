#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def reload(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    del value['__class__']

                    # Dynamically get the class by name
                    class_ = globals()[class_name]
                    obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def save(self):
        """Serialize the objects to a JSON file."""
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            data = {}
            for key, obj in self.__objects.items():
                data[key] = obj.to_dict()
            json.dump(data, file)

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects
