import sys
import os
import magic

def file_command(file_name):
    file_path = os.getcwd() + '/' + file_name
    if(os.path.exists(file_path) == False):
        print(file_name + ': Cannot open \'' + file_name + '\' (No such file or directory)')
    else:
        print(file_name + ': ' + magic.from_file(file_name))

if(sys.argv[1] == '--help'):
    f = open('help_files/help_file.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "man"):
    f = open('man_files/man_file.txt', 'r')
    print(f.read())
else:
    file_command(sys.argv[1])