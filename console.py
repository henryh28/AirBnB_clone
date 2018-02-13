#!/usr/bin/python3
""" Entry point for the command interpreter """

import cmd
import models
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}
forbidden = {"id", "created_at", "updated_at"}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    do_EOF = do_quit
    do_eof = do_quit

    def emptyline(self):
        """ Do nothing if no input is entered """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to JSON file and
        prints the id
        """
        if not arg:
            print("** class name missing **")
        if arg in classes:
            obj = classes[arg]()
            print (obj.id)
            obj.save()
        else:
            print("** class doesn't exist **")

    def error_check(self, args):
        """ DRY method for error checking for other functions """
        args_list = args.split()

        if not args:
            print("** class name missing **")
            return 1
        if args_list[0] not in classes:
            print("** class doesn't exist **")
            return 1
        if len(args_list) < 2:
            print("** instance id missing **")
            return 1

        obj = args_list[0] + "." + args_list[1]
        if obj not in models.storage.all():
            print("** no instance found **")
            return 1

        return (obj)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class
        name and id
        """
        obj = self.error_check(args)

        if obj == 1:
            return
        if obj in models.storage.all():
            print(models.storage.all()[obj])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        obj = self.error_check(args)
        if obj == 1:
            return
        if obj in models.storage.all():
            models.storage.all().pop(obj)
            models.storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances base or not on the\
        class name
        """
        args_list = args.split()
        comma_flag = 0
        output = "["

        if (len(args_list) > 0) and args_list[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args_list) == 0:
            for value in models.storage.all().values():
                output += ", " if comma_flag == 1 else ""
                output += str(value)
                comma_flag = 1
        elif len(args_list) > 0:
            for value in models.storage.all().values():
                if value.__class__.__name__ == args_list[0]:
                    output += ", " if comma_flag == 1 else ""
                    output += str(value)
                    comma_flag = 1

        output += "]"
        print(output)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        args_list = args.split()
        obj = self.error_check(args)

        if obj == 1:
            return
        if len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            if (args_list[2] not in forbidden):
                obj_dict = models.storage.all()[obj].to_dict()

                if type(args_list[3]) is str:
                    args_list[3] = args_list[3].strip('"')
                obj_dict[args_list[2]] = args_list[3]
                models.storage.all()[obj].save()
            else:
                print("[Skynet]: Human please don't change that attribute")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
