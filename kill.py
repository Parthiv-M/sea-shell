import psutil
import sys

def kill(pid):
    p = psutil.Process(pid)
    p.terminate()

if(sys.argv[1] == '--help'):
    f = open('help_files/help_kill.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "man"):
    f = open('man_files/man_kill.txt', 'r')
    print(f.read())
else:
    kill(sys.argv[1])