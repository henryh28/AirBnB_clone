#!/usr/bin/python3
""" Entry point for the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    do_EOF = do_quit

    def emptyline(self):
        """ Do nothing if no input is entered """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
