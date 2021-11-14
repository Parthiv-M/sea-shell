import os
import sys

def makedir(directory,dir_name):
    """Function to take a parent directory, directory name, permissions as parameters and create a directory at the specified parent directory."""
    path = os.path.join(directory,dir_name)
    os.mkdir(path)
    print("Directory created successfully!\n")

if(sys.argv[1] == '--help'):
    f = open('help_files/help_mkdir.txt', 'r')        
    print(f.read())
elif(sys.argv[1] == "man"):
    f = open('man_files/man_mkdir.txt', 'r')        
    print(f.read())
else:
    makedir(sys.argv[1], sys.argv[2])