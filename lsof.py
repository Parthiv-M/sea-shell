import psutil
import os
import sys

def if_not_exists(dir_path):
    if(os.path.exists(dir_path) == False):
        print('Cannot open \'' + dir_path + '\' (No such file or directory)')
        sys.exit()

def is_open_file(fpath):
    for proc in psutil.process_iter():
        try:
            for item in proc.open_files():
                if fpath == item.path:
                    return proc
        except Exception:
            pass
    return None
# base_path = '/home/rithika/Downloads/'
def lsof(dir_path):
    if_not_exists(dir_path)
    entries = os.listdir(dir_path)
    for entry in entries:
        p = is_open_file(dir_path + '/' + entry)
        if not p == None:
            print(entry + ' \n--Opened by process = '+ p.name() + '\n--PID = ' + str(p.pid) + '\n')

if(sys.argv[1] == '--help'):
    f = open('help_files/help_lsof.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "man"):
    f = open('man_files/man_lsof.txt', 'r')
    print(f.read())
else:
    lsof(sys.argv[1])

