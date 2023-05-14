#!/usr/bin/python3
"""Module replicates CLI."""
import cmd
import json
import shlex as sh
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Empty class created.
    Class inherits from cmd.Cmd."""

    intro = 'Welcome to the hbnb shell.'
    prompt = '(hbnb) '

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def _precmd(self, line):
        pass

    def do_create(self, line):
        """Creates new instance of BaseModel."""

        if not line:
            print("** class name missing **")
            return
        token = sh.split(line)
        if token[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.__classes[token[0]]()
        storage.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints string representation
        of an instance."""
        token = sh.split(line)
        if len(token) == 0:
            print("** class name missing **")
            return
        if token[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
            return
        if len(token) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        all_obj = storage.all()
        key = token[0] + "." + token[1]
        if key in all_obj:
            obj_instance = str(all_obj[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance."""

        token = sh.split(line)
        if len(token) == 0:
            print("** class name missing **")
            return
        if token[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
            return
        storage.reload()
        all_obj = storage.all()
        key = token[0] + "." + token[1]
        if key in all_obj:
            del all_obj[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation
        of all instances."""
        
        storage.reload()
        obj_list = []
        all_obj = storage.all()
        if not line:
            for key in all_obj:
                obj_list.append(str(all_obj[key]))
            print(json.dumps(obj_list))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance."""

        if not line:
            print("** class name missing **")
            return
        token = sh.split(line)
        storage.reload()
        all_obj = storage.all()
        if token[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
            return
        if (len(token) == 1):
            print("** instance id missing **")
            return
        try:
            key = token[0] + "." + token[1]
            all_obj[key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(token) == 2):
            print("** attribute name missing **")
            return
        if (len(token) == 3):
            print("** value missing **")
            return
        my_instance = all_obj[key]
        if hasattr(my_instance, token[2]):
            data_type = type(getattr(my_instance, token[2]))
            setattr(my_instance, token[2], data_type(token[3]))
        else:
            setattr(my_instance, token[2], token[3])
        storage.save()


    def do_EOF(self, line):
        """Exits the program."""
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
