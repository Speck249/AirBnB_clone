#!/usr/bin/python3
"""Module replicates CLI."""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Empty class created.
    Class inherits from cmd.Cmd."""

    intro = 'Welcome to the hbnb shell.'
    prompt = '(hbnb)'

    def _precmd(self, line):
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel."""
        pass

    def do_show(self, line):
        """Prints string representation
        of an instance."""
        pass

    def do_destroy(self, line):
        """Deletes an instance."""
        pass

    def do_all(self, line):
        """Prints all string representation
        of all instances."""
        pass

    def do_update(self, line):
        """Updates an instance."""
        pass

    def do_EOF(self, line):
        """Exits the program."""
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
