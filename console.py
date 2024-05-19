#!/usr/bin/python3
"""
This module defines the HBNBCommand class which is the command interpreter
for the HBNB project.
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB.
    Provides a prompt and commands to interact with the system.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program with EOF (Ctrl-D).
        Usage: EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        Overrides the default behavior of repeating the last command.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
