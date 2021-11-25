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
                procs_info = proc.as_dict(attrs = ['pid','name','cpu_percent', 'cmdline'])
                if fpath == item.path:
                    if psutil.Process()==proc: print("yes")
                    return proc
                elif fpath in procs_info['cmdline']:
                    return proc
        except Exception:
            pass
    return False

# base_path = '/home/rithika/Downloads'
def lsof(dir_path):
    if_not_exists(dir_path)
    entries = os.listdir(dir_path+'/')
    for entry in entries:
        p = is_open_file(dir_path+'/'+entry)
        if not p == False:
            print(entry+' \n--Opened by process = '+p.name()+'\n--PID = '+str(p.pid)+'\n')

def lsof_cur():
    dir_path = os.getcwd()
    entries = os.listdir(dir_path+'/')
    for entry in entries:
        p = is_open_file(dir_path+'/'+entry)
        if not p == False:
            print(entry+' \n--Opened by process = '+p.name()+'\n--PID = '+str(p.pid)+'\n')

if(len(sys.argv)==1): 
    lsof_cur()
elif(len(sys.argv)==2):
    if(sys.argv[1] == '--help'):
        f = open('help_files/help_free.txt', 'r')
        print(f.read())
    elif(sys.argv[1] == "man"):
        f = open('man_files/man_free.txt', 'r')
        print(f.read())
    else:
        lsof(sys.argv[1])
        
# lsof_cur()

