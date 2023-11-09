#!/usr/bin/python3
"""This is console Module
contains the entry point of the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_list = ['BaseModel']

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """A Method to do nothing when an empty line is
        entered by the user
        """
        pass

    def postloop(self):
        """method to do nothing after each console loop.
        """
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id

        Arguments:
            args (str): the inputed argement in command prompt
        """
        line = args.split()
        if not self.verify_class(line):
            return
        instance = eval(line[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    def do_show(self, args):
        """Print the string representation of an instance
        based on the class name and id.

        Arguments:
            args (str): the inputed argement in command prompt
        """
        line = args.split()
        # verify class
        if not self.verify_class(line):
            return
        # verify id
        if not self.verify_id(line):
            return
        key = '{}.{}'.format(line[0], line[1])
        objects = models.storage.all()
        print(objects[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Arguements:
            args (str): the inputed argement in command prompt
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        key = '{}.{}'.format(line[0], line[1])
        objects = models.storage.all()
        del objects[key]
        models.storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        line = args.split()
        objects = models.storage.all()
        to_print = []
        if len(line) == 0:
            for v in objects.values():
                to_print.append(str(v))
        elif line[0] in HBNBCommand.class_list:
            for k, v in objects.items():
                if line[0] in k:
                    to_print.append(str(v))
        else:
            print("** class doesn't exist **")
            return False
        print(to_print)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        if not self.verify_attribute(line):
            return
        objects = models.storage.all()
        key = '{}.{}'.format(line[0], line[1])
        setattr(objects[key], line[2], line[3])
        models.storage.save()

    @classmethod
    def verify_class(cls, line):
        """class method to verify class instance
        """
        if len(line) == 0:
            print("** class name missing **")
            return False
        elif line[0] not in HBNBCommand.class_list:
            print('** class doesn\'t exist **')
            return False
        return True

    @staticmethod
    def verify_id(line):
        """static method to verify the id of class instance
        """
        if len(line) < 2:
            print('** instance id missing **')
            return False
        objects = models.storage.all()
        key = '{}.{}'.format(line[0], line[1])
        if key not in objects.keys():
            print('** no instance found **')
            return False
        return True

    @staticmethod
    def verify_attribute(line):
        """Static method to verify the attribute in inputted line.
        """
        if len(line) < 3:
            print("** attribute name missing **")
            return False
        elif len(line) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
