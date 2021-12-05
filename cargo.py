import psutil
import os
import sys

def if_not_exists(dir_path):

    """
    Function to check if the given directory path exists
    ...
    Parameters
    ----------
    dir_path : str
        Path of the directory
    """

    if(os.path.exists(dir_path) == False):
        print('Cannot open \'' + dir_path + '\' (No such file or directory)')
        sys.exit()

def is_open_file(fpath):

    """
    Function to check if a file is open or not
    ...
    Parameters
    ----------
    fpath : str
        Name or path of the file to check for
    """

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

def lsof(dir_path):

    """
    Function to list all the open processes
    ...
    Parameters
    ----------
    dir_path : str
        Path of the directory to search open processes for
    """

    if_not_exists(dir_path)
    entries = os.listdir(dir_path+'/')
    for entry in entries:
        p = is_open_file(dir_path+'/'+entry)
        if not p == False:
            print(entry+' \n--Opened by process = '+p.name()+'\n--PID = '+str(p.pid)+'\n')

def lsof_cur():

    """
    Function to check for open processes or applications in the current directory
    """

    dir_path = os.getcwd()
    entries = os.listdir(dir_path + '/')
    for entry in entries:
        p = is_open_file(dir_path + '/' + entry)
        if not p == False:
            print(entry + ' \n--Opened by process = ' + p.name() + '\n--PID = ' + str(p.pid) + '\n')

if(len(sys.argv) == 1): 
    lsof_cur()
elif(len(sys.argv) == 2):
    if(sys.argv[1] == '--help'):
        f = open('help_files/help_lsof.txt', 'r')
        print(f.read())
    elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
        print("lsof (sea shell) 1.0.0")
    elif(sys.argv[1] == "treasure-map"):
        f = open('man_files/man_lsof.txt', 'r')
        print(f.read())
    else:
        lsof(sys.argv[1])