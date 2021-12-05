import os
import sys

def pwd():

    """
    Function to print the current working directory of the shell
    """

    print(os.getcwd())

if(len(sys.argv) == 1):
    pwd()
elif(len(sys.argv) == 2):
    if(sys.argv[1] == '--help'):
        f = open('help_files/help_pwd.txt', 'r')
        print(f.read())
    elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
        print("pwd (sea shell) 1.0.0")
    elif(sys.argv[1] == "treasure-map"):
        f = open('man_files/man_pwd.txt', 'r')
        print(f.read())
    