#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        serialized = {}
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                loaded = json.load(file)
                for key, value in loaded.items():
                    class_name = value['__class__']
                    del value['__class__']
                    obj = FileStorage.__objects[class_name](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
