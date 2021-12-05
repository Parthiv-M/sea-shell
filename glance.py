import sys
import os

def if_not_exists(file_name):
    
    """
    Function to check if the file with a given file name exists or not
    ...
    Parameters
    ----------
    file_name : str
        File name of the file to check for existence
    """
    
    file_path = os.getcwd() + '/' + file_name
    if(os.path.exists(file_path) == False):
        print(file_name + ': Cannot open \'' + file_name + '\' (No such file or directory)')
        sys.exit()

def cat(f_name):    
    
    """
    Function to take a file name and print out the contents of the file
    ...
    Parameters
    ----------
    f_name : str
        File name of the file to print contents of 
    """
    
    if f_name.startswith('>'):
        file_name = f_name[1:]
        if_not_exists(file_name)
        f = open(file_name, 'a')
        i = input()
        f.write(i)
    elif ">>" in f_name:
        file_name = f_name.split('>>')
        if_not_exists(file_name[1])
        f1 = open(file_name[0], 'r')
        f2 = open(file_name[1], 'a')
        i = f1.read()
        f2.write(i)
    else:
        file_name = f_name
        if_not_exists(file_name)
        f = open(file_name)
        i = f.read()
        print(i)

if(sys.argv[1] == '--help'):
    f = open('help_files/help_cat.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("cat (sea shell) 1.0.0")
elif(sys.argv[1] == "treasure-map"):
    f = open('man_files/man_cat.txt', 'r')
    print(f.read())
else:
    cat(sys.argv[1])


    