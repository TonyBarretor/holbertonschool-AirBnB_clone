#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for Holberton Airbnb project."""

    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to JSON file."""
        if not arg:
            print("** class name missing **")
            return

        try:
            class_type = eval(arg)()
            class_type.save()
            print(class_type.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = FileStorage().all()
        obj = objects.get(key, None)

        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = FileStorage().all()
        obj = objects.get(key, None)

        if obj:
            del objects[key]
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        objects = FileStorage().all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_type = eval(arg)
                print([str(obj) for key, obj in objects.items() if type(obj) == class_type])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = FileStorage().all()
        obj = objects.get(key, None)

        if obj:
            setattr(obj, args[2], args[3])
            obj.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
