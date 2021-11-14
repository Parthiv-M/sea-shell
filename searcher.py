import os
import sys

def searcher(paths, word):
    for path in paths:
        ind = path.find(word)
        if(ind != -1):
            print(path)
            break
        else:
            print("Could not find a file that contains your file name")
            break

def file_searcher(root, word):
    filePaths = []
    print("Searching for files...")
    for root, dirs, files in os.walk(root):
        for f in files:
            filePaths.append(os.path.join(root, f))
    print(filePaths)
    searcher(filePaths, word)

filename = sys.argv[1]

if(sys.argv[1] == '--help'):
    f = open('help_files/help_searcher.txt', 'r')        
    print(f.read())
elif(sys.argv[1] == "man"):
    f = open('man_files/man_searcher.txt', 'r')        
    print(f.read())
else:
    file_searcher('/home/parthiv/Desktop', sys.argv[1])
