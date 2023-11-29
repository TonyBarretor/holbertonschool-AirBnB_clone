#!/usr/bin/python3
"""
Console module for AirBnB clone project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for handling the command-line interface.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def help_quit(self):
        """Print help message for quit command."""
        print("Quit command to exit the console.")

    def do_EOF(self, arg):
        """Handle EOF signal."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass


if _name_ == '_main_':
    HBNBCommand().cmdloop()
