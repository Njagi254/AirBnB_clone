#!/usr/bin/python3
"""
Entry point for the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for managing HBNB objects
    """
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        End of File command to exit the program
        """
        print()  # Print a newline character for better formatting upon EOF
        return True

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it, and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances
        """
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in storage.all().values():
            if not arg or (arg and type(obj).__name__ == arg):
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        # Casting value to appropriate type
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
        else:
            setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, line):
        """
        Handle unrecognized commands, such as <class name>.all(),
        <class name>.count(), and <class name>.show(<id>)
        """
        args = line.split('.')
        if len(args) > 1:
            class_name = args[0]
            command = args[1]
            if class_name in self.classes:
                if command == "all()":
                    self.do_all(class_name)
                elif command == "count()":
                    self.count(class_name)
                elif command.startswith("show(") and command.endswith(")"):
                    instance_id = command[5:-1].strip('"')
                    self.do_show(f"{class_name} {instance_id}")
                elif command.startswith("destroy(") and command.endswith(")"):
                    instance_id = command[8:-1].strip('"')
                    self.do_destroy(f"{class_name} {instance_id}")
                elif command.startswith("update(") and command.endswith(")"):
                    update_args = command[7:-1]
                    args = update_args.split(', ')
                    if len(args) != 3:
                        print("** invalid number of arguments **")
                        return
                    instance_id = args[0].strip('"')
                    attr_name = args[1].strip('"')
                    attr_value = args[2].strip('"')
                    self.do_update(
                        f"{class_name} {instance_id} {attr_name} {attr_value}"
                        )
                else:
                    print("*** Unknown syntax: {}".format(line))
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))

    def count(self, class_name):
        """
        Retrieve the number of instances of a class
        """
        count = sum(
            1 for obj in storage.all().values() if type(obj).__name__
            == class_name)
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
