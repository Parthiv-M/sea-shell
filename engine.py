import psutil
import sys

def free_proc(pid):

    """
    Function to take process ID and display memory usage details of the process.
    ...
    Parameters
    ----------
    pid : number
        Process ID of the file to display details
    """

    flag = 0
    for proc in psutil.process_iter():
        if pid == proc: flag = 1
    if flag == 0: 
        print('The given PID is not a valid PID of a running process:\'',pid,'\'')
        return
    proc = psutil.Process(pid)
    print('Memory info of Process \'', pid,'\':')
    mem = proc.memory_info()
    print('VM memory used by process: ', mem.vms)
    print('Shared Memory Usage: ', mem.shared)
    print('Percentage of memory used by Process: ', proc.memory_percent())

def free():

    """
    Function to display memory usage details of all processes.
    """

    vm = psutil.virtual_memory()
    sm = psutil.swap_memory()
    print('   \tTotal\t\tUsed\t\tFree\t\tBuffers\t\tCached\t\tShared\t\t\n')
    print('Mem: \t',vm.total,'\t',vm.used,'\t',vm.free,'\t',vm.buffers,'\t',vm.cached,'\t',vm.shared)
    print('Swap:\t',sm.total,'\t',sm.used,'\t',sm.free)


if(len(sys.argv) == 1):
    free()
elif(len(sys.argv) == 2):
    if(sys.argv[1] == '--help'):
        f = open('help_files/help_free.txt', 'r')
        print(f.read())
    elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
        print("free (sea shell) 1.0.0")
    elif(sys.argv[1] == "treasure-map"):
        f = open('man_files/man_free.txt', 'r')
        print(f.read())
    else: 
        free_proc(sys.argv[1])