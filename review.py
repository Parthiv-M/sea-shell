import requests
import sys

def spell_check(fname):

    """
    Function to read a text file one word at a time and check for spelling mistakes, if found report the mistake and provide a suggestion.
    ...
    Parameters
    ----------
    fname : str
        The name of the file to check for spelling mistakes
    """
    
    base_url = "https://api.textgears.com/spelling"
    params = {"key" : "7Py3b8Y9cVjEeAp1", "text" : ""}
    txt_fl = open(fname,'r')
    lines = txt_fl.readlines()
    flag = 0
    for lin_no in range(len(lines)):
        line = lines[lin_no].strip()
        words = line.split()
        for ind in range(len(words)):
            params["text"] = words[ind]
            ret_obj = requests.get(base_url,params = params)
            ret = ret_obj.json()
            if ret["response"]["errors"] == []:
                continue
            else:
                print("Bad spelling at line {}, word {}".format(lin_no,ind))
                sgstn = ret["response"]["errors"][0]["better"][0]
                print("Did you mean {} ?\n".format(sgstn))
                flag = 1
                break
        if flag == 1:
            break

if(sys.argv[1] == '--help'):
    f = open('help_files/help_checker.txt', 'r')
    print(f.read())
elif(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
    print("checker (sea shell) 1.0.0")
elif(sys.argv[1] == "treasure-map"):
    f = open('man_files/man_checker.txt', 'r')
    print(f.read())
else:
    spell_check(sys.argv[1])
