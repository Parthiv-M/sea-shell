import sys
import psutil

def ps():

    """
    Function to print the processes running on the system with their process IDs.
    """

    print("PID\t\tNAME\t\t\t\t\t\tCPU%")
    print('---------------------------------------------------------------------')
    for proc in psutil.process_iter():
        procs_info = proc.as_dict(attrs = ['pid','name','cpu_percent'])
        print("{}\t\t{:40s}\t{}".format(procs_info['pid'], procs_info['name'], procs_info['cpu_percent']))

if(len(sys.argv) == 1):
    ps()
elif(len(sys.argv) == 2):
    if(sys.argv[1] == '--help'):
        f = open('help_files/help_ps.txt', 'r')
        print(f.read())
    elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
        print("ps (sea shell) 1.0.0")
    elif(sys.argv[1] == "treasure-map"):
        f = open('man_files/man_ps.txt', 'r')
        print(f.read())

