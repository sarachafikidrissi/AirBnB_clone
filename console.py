#!/usr/bin/python3
"""This is console Module
contains the entry point of the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                  'Review']

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

    def default(self, args):
        """ A method that is called when the entered command starts
        with a class name.

        Attributes:
            args (str): The entered line string
        """
        line = args.strip('()').split(".")
        if len(line) < 2:
            print('** missing attribute **')
            return
        objects = models.storage.all()
        cls_name = line[0].capitalize()
        cmd_name = line[1].lower()
        split2 = cmd_name.strip(')').split('(')
        cmd_name = split2[0]
        if cmd_name == 'all':
            HBNBCommand.do_all(self, cls_name)
        elif cmd_name == 'count':
            count = 0
            for k in objects.keys():
                key = k.split('.')
                if cls_name == key[0]:
                    count += 1
            print(count)
        elif cmd_name == 'show':
            if len(split2) < 2:
                print('** no instance found **')
            else:
                HBNBCommand.do_show(self, cls_name + ' ' + split2[1])
        elif cmd_name == 'destroy':
            if len(split2) < 2:
                print('** no instance found **')
            else:
                HBNBCommand.do_destroy(self, cls_name + ' ' + split2[1])
        elif cmd_name == 'update':
            split3 = split2[1].split(', ')
            if len(split3) == 0:
                print('** no instance found **')
            elif len(split3) == 1 and type(split3[1]) == dict:
                for k, v in split[1].items():
                    HBNBCommand.do_update(self, cls_name + ' ' + split3[0] +
                                          ' ' + k + ' ' + v)
            elif len(split3) == 1 and type(split3[1]) != dict:
                print('** no instance found **')
            elif len(split3) == 2:
                print('** no instance found **')
            else:
                HBNBCommand.do_update(self, cls_name + ' ' + split3[0] +
                                      ' ' + split3[1] + ' ' + split3[2])

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
