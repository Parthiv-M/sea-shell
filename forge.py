import os
import sys

def makedir(directory, dir_name):

    """
    Function to take a parent directory, directory name, permissions as parameters and create a directory at the specified parent directory.
    ...
    Parameters
    ----------
    directory : str 
        parent directory to create the new directory
    dir_name : str 
        name for the new directory being created 
    """

    path = os.path.join(directory,dir_name)
    os.mkdir(path)
    print("Directory created successfully!\n")

if(sys.argv[1] == '--help'):
    f = open('help_files/help_mkdir.txt', 'r')        
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("mkdir (sea shell) 1.0.0")
elif(sys.argv[1] == "treasure-map"):
    f = open('man_files/man_mkdir.txt', 'r')        
    print(f.read())
else:
    makedir(sys.argv[1], sys.argv[2])