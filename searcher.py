import os
import sys

def searcher(paths, word):
    print(word)
    for p in paths:
        if(p.find(word) != -1):
            print("Path of your file is: " + p)
            return
    print("Could not find a file that contains your file name")

def file_searcher(root, word):
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
elif(sys.argv[1] == "man"):
    f = open('man_files/man_searcher.txt', 'r')        
    print(f.read())
else:
    file_searcher('/', sys.argv[1])
