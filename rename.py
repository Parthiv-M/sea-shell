import os
import sys

def rnm(old_nm, new_nm):
    
    """
    Function to rename an existing file or directory
    ...
    Parameters
    ----------
    old_nm : str 
        Old name of the file or directory
    new_nm : str 
        New name of the file or directory
    """
    
    os.rename(old_nm,new_nm);
    print("Rename successful!\n")

if(sys.argv[1] == '--help'):
    f = open('help_files/help_rename.txt', 'r')        
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("rename (sea shell) 1.0.0")
elif(sys.argv[1] == "treasure-map"):
    f = open('man_files/man_rename.txt', 'r')        
    print(f.read())
else:
    rnm(sys.argv[1], sys.argv[2])