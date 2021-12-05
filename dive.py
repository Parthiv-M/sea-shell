import os
import sys

def searcher(paths, word):

    """
    Function to search for a file in the entire file system, by any part of the file name
    ...
    Parameters
    ----------
    paths : list
        A list containing all the file paths of the file system
    word : str
        File name or part of the file name to search for 
    """

    print(word)
    for p in paths:
        if(p.find(word) != -1):
            print("Path of your file is: " + p)
            return
    print("Could not find a file that contains your file name")

def file_searcher(root, word):

    """
    Function to create a list of the file path of the file system
    ...
    Parameters
    ----------
    root : str
        Path of the root directory to start searching from
    word : str
        File name or part of the file name to search for
    """

    filePaths = []
    print("Searching for files...")
    for root, dirs, files in os.walk(root):
        for f in files:
            filePaths.append(os.path.join(root, f))
    searcher(filePaths, word)

filename = sys.argv[1]

if(sys.argv[1] == '--help'):
    f = open('help_files/help_searcher.txt', 'r')        
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("searcher (sea shell) 1.0.0")
elif(sys.argv[1] == "treasure-map"):
    f = open('man_files/man_searcher.txt', 'r')        
    print(f.read())
else:
    file_searcher('/', sys.argv[1])
