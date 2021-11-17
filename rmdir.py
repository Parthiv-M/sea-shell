import os
import sys

def remdir(directory, dir_name):
    
    """
    Function to take a parent directory, directory name as parameters and remove a directory at the specified parent directory.
    ...
    Parameters
    ----------
    directory : str 
        Name of the parent directory
    """
    
    path = os.path.join(directory,dir_name)
    os.rmdir(path)
    print("Directory removed successfully!\n")

if(sys.argv[1] == '--help'):
    f = open('help_files/help_rmdir.txt', 'r')        
    print(f.read())
elif(sys.argv[1] == "man"):
    f = open('man_files/man_rmdir.txt', 'r')        
    print(f.read())
else:
    remdir(sys.argv[1], sys.argv[2])