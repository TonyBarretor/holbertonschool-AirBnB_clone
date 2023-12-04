#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB Airbnb project
    """
    prompt = '(hbnb) '
    # ... other methods ...
    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = line.split()
        all_objects = storage.all()
        if not args:
            print([str(obj) for obj in all_objects.values()])
        elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            print([str(obj) for key, obj in all_objects.items() if class_name in key])
    def default(self, line):
        """Called on an input line when the command prefix is not recognized
        """
        parts = line.split(".")
        if len(parts) == 2 and parts[1] == "all()":
            class_name = parts[0]
            all_instances = storage.all().values()
            filtered_instances = [str(instance) for instance in all_instances if isinstance(instance, eval(class_name))]
            print(filtered_instances)
        else:
            print("*** Unknown syntax:", line)
# ... other methods ...
if __name__ == '__main__':
    HBNBCommand().cmdloop()
