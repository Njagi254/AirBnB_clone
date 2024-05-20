#!/usr/bin/python3
"""
Command interpreter module
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB
    """
    prompt = '(hbnb) '

    def do_create(self, args):
        """Creates a new instance of BaseModel or User, saves it (to the JSON file) and prints the id."""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        obj_list = []
        if args:
            if args not in storage.classes():
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if args in key:
                    obj_list.append(str(value))
        else:
            for key, value in storage.all().items():
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(tokens) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(tokens[0], tokens[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(tokens) == 2:
            print("** attribute name missing **")
            return
        if len(tokens) == 3:
            print("** value missing **")
            return
        instance = storage.all()[key]
        setattr(instance, tokens[2], tokens[3].strip('"'))
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()