from os import system

# For autocomplete and suggestions
from fuzzywuzzy import fuzz

shell_commands = [
    "help", 
    "man", 
    "searcher", 
    "file", 
    "checker", 
    "mkdir", 
    "rmdir", 
    "rename", 
    "free",
    "ps",
    "tree",
    "clear", 
    "exit"
]

def closest_command_finder(command):

    """
    Function to take a command string, find the closest matching command and return a possible match from the existing set of shell commands.
    ...
    Parameters
    ----------
    command : str 
        The command to be analysed to find the closest match
    """

    closest_command = command
    sys_command = shell_commands[0]
    fuzzratio = fuzz.ratio(command, sys_command)
    for sys_command in shell_commands:
        if fuzz.ratio(command, sys_command) > fuzzratio and fuzz.ratio(command, sys_command)!=0:
            fuzzratio = fuzz.ratio(command, sys_command)
            closest_command = sys_command

    return closest_command

def shell_help():

    """
    Function to display the help text for the shell on startup.
    """

    f = open('startup_files/startup.txt', 'r')        
    print(f.read())
    print('\n')

def shell():

    """
    Function that runs the shell.
    """

    startup = 1
    from_cmd_error = 0

    while 1:
        if startup == 1:
            startup = startup + 1
            _ = system('clear')
            shell_help()        
        
        if (from_cmd_error == 0):
            userinput = input("\033[1msea-shell@\033[94muser\033[0m$ ")
            pass
        else:
            userinput = closest_command + " " + userinput
            from_cmd_error = 0
        
        input_arr = userinput.split()

        if(input_arr[0] == shell_commands[0]): # shell help
            shell_help()
        elif(len(input_arr) == 1 and (input_arr[0] in shell_commands) and input_arr[0] != 'exit' and input_arr[0] != 'clear' and input_arr[0] != 'free' and input_arr[0] != 'ps'):
            system('python3 ' + input_arr[0] + '.py --help')
        elif(input_arr[0] == shell_commands[1]):
            system('python ' + input_arr[1] + '.py ' + input_arr[0]) # man page for every command
        elif(input_arr[0] == shell_commands[2]):  # file searcher command
            system('python3 searcher.py ' + input_arr[1])
        elif(input_arr[0] == shell_commands[3]):  # file command
            system('python3 file.py ' + input_arr[1])
        elif(input_arr[0] == shell_commands[4]):  # spell checker command
            system('python3 checker.py ' + input_arr[1])
        elif(input_arr[0] == shell_commands[5]):  # make directory command
            if len(input_arr) == 3:
                system('python3 mkdir.py ' + input_arr[1] + input_arr[2])
            elif len(input_arr) == 2:
                system('python3 mkdir.py ' + input_arr[1])
        elif(input_arr[0] == shell_commands[6]):  # remove directory command
            if len(input_arr) == 3:
                system('python3 rmdir.py ' + input_arr[1] + input_arr[2])
            elif len(input_arr) == 2:
                system('python3 rmdir.py ' + input_arr[1])
        elif(input_arr[0] == shell_commands[7]):  # rename command
            if len(input_arr) == 3:
                system('python3 rename.py ' + input_arr[1] + input_arr[2])
            elif len(input_arr) == 2:
                system('python3 rename.py ' + input_arr[1])
        elif(input_arr[0] == shell_commands[8]):  # free command
            if len(input_arr) == 3:
                system('python3 free.py ' + input_arr[1] + input_arr[2])
            elif len(input_arr) == 2:
                system('python3 free.py ' + input_arr[1])
            elif len(input_arr) == 1:
                system('python3 free.py')
        elif(input_arr[0] == shell_commands[9]):  # ps command
            if len(input_arr) == 2:
                system('python3 ps.py ' + input_arr[1])
            else: 
                system('python3 ps.py')
        elif(input_arr[0] == shell_commands[10]):  # tree command
            if len(input_arr) == 2:
                system('python3 tree.py ' + input_arr[1])
        elif(input_arr[0] == shell_commands[11]):  # clear command
            _ = system('clear')
        elif(input_arr[0] == shell_commands[12]):  # exit command
            exit(0)
        else:
            closest_command = closest_command_finder(input_arr[0])
            userinput = input(input_arr[0] + ": command not found. Did you mean " + closest_command + "? (y/n): ")
            if userinput == 'y' or userinput == 'Y':
                userinput = input("\033[1msea-shell@\033[94muser\033[0m$ " + closest_command)
                from_cmd_error = 1;
            else:
                continue

shell()