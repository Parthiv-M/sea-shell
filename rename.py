import os
import sys

def rnm(old_nm, new_nm):
    os.rename(old_nm,new_nm);
    print("Rename successful!\n")

if(sys.argv[1] == '--help'):
    f = open('help_files/help_rename.txt', 'r')        
    print(f.read())
elif(sys.argv[1] == "man"):
    f = open('man_files/man_rename.txt', 'r')        
    print(f.read())
else:
    rnm(sys.argv[1], sys.argv[2])