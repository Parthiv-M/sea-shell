from os import system

shell_commands = ["help", "man", "searcher", "file", "checker", "mkdir", "rmdir", "rename", "clear", "exit"]

def shell_help():
    print("I am supposed to help the user")

def shell():
    startup = 1
    while 1:
        if startup == 1:
            startup = startup + 1
            _ = system('clear')

        # add code for startup of shell here
        
        userinput = input("\033[1msea-shell@\033[94muser\033[0m$ ")
        input_arr = userinput.split()

        if(input_arr[0] == shell_commands[0]): # shell help
            shell_help()
        elif(len(input_arr) == 1 and (input_arr[0] in shell_commands) and input_arr[0] != 'exit' and input_arr[0] != 'clear'):
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
            if len(input_arr) == 2:
                system('python3 rmdir.py ' + input_arr[1])
        elif(input_arr[0] == shell_commands[7]):  # rename command
            if len(input_arr) == 3:
                system('python3 rename.py ' + input_arr[1] + input_arr[2])
            if len(input_arr) == 2:
                system('python3 rename.py ' + input_arr[1])
        elif(input_arr[0] == shell_commands[8]):
            _ = system('clear')
        elif(input_arr[0] == shell_commands[9]):
            exit(0)

shell()