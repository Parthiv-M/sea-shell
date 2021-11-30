import psutil, sys

def kill(pid):
    for proc in psutil.process_iter():
        procs_info = proc.as_dict(attrs = ['pid','name','cpu_percent', 'cmdline'])
        try:
            if(procs_info['pid'] == int(pid)) :
                p = psutil.Process(int(pid))
                p.kill()
        except:
            pass
    print("Error : kill (%s) -- No such process"%(pid))

if(len(sys.argv)==2):
    if(sys.argv[1] == '--help'):
        f = open('help_files/help_kill.txt', 'r')
        print(f.read())
    elif(sys.argv[1] == "man"):
        f = open('man_files/man_kill.txt', 'r')
        print(f.read())
    else:
        kill(sys.argv[1])