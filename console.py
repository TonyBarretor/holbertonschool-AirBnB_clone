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
    def do_create(self, line):
        """Create a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        else:
            classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
            if line not in classes:
                print("** class doesn't exist **")
            else:
                new_instance = eval(line)()
                new_instance.save()
                print(new_instance.id)
    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                print(all_objects[key])
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                del all_objects[key]
                storage.save()
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
            print([str(obj) for key, obj in all_objects.items() if args[0] in key])

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



    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change
        into the JSON file)
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = all_objects[key]
                setattr(obj, args[2], eval(args[3]))
                storage.save()
    def do_EOF(self, line):
        """Exits the console
        """
        return True
    def do_quit(self, line):
        """Exits the console
        """
        return True
    def emptyline(self):
        """Empty line + ENTER should not execute anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
