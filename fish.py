import sys
import os
import magic

def file_command(file_name):

    """
    Function to find out information about the file
    ...
    Parameters
    ----------
    file_name : str
        The name of the file to extract information
    """

    file_path = os.getcwd() + '/' + file_name
    if(os.path.exists(file_path) == False):
        print(file_name + ': Cannot open \'' + file_name + '\' (No such file or directory)')
    else:
        print(file_name + ': ' + magic.from_file(file_name))

if(sys.argv[1] == '--help'):
    f = open('help_files/help_file.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("file (sea shell) 1.0.0")
elif(sys.argv[1] == "treasure-map"):
    f = open('man_files/man_file.txt', 'r')
    print(f.read())
else:
    file_command(sys.argv[1])