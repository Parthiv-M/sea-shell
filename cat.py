import sys
import os
def if_not_exists(file_name):
    file_path = os.getcwd() + '/' + file_name
    if(os.path.exists(file_path) == False):
        print(file_name + ': Cannot open \'' + file_name + '\' (No such file or directory)')
        sys.exit()
def cat(str):    
    if str.startswith('>'):
        file_name = str[1:]
        if_not_exists(file_name)
        f = open(file_name, 'a')
        i = input()
        f.write(i)
    elif ">>" in str:
        file_name = str.split('>>')
        if_not_exists(file_name[1])
        f1 = open(file_name[0], 'r')
        f2 = open(file_name[1], 'a')
        i = f1.read()
        f2.write(i)
    else:
        file_name = str
        if_not_exists(file_name)
        f = open(file_name)
        i = f.read()
        print(i)

if(sys.argv[1] == '--help'):
    f = open('help_files/help_cat.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "man"):
    f = open('man_files/man_cat.txt', 'r')
    print(f.read())
else:
    cat(sys.argv[1])


    