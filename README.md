# SEA SHELL

A custom *Lost at Sea* themed Linux shell that contains several default Linux commands as well as a few custom commands that we found as a necessary addition to the shell. We used Python 3.6.9 to build this custom shell.

# What is a shell?
A shell, although not part of the operating system, is the primary interface between the user and an operating system. It gathers inputs from a user (command line interpreter), executes programs based on the input by making system calls to the kernel, and displays corresponding outputs. The shell being the outermost layer of any operating system incorporates a programming language to control processes and files, as well as to start and control other programs. 

# Setting up the sea shell

### Prerequisties
- A working python installation with either `pip` or `conda`, at least Python version >= 3.6. Verify the installation by running `python3 -V`. If not, install python from [here]()
- Access to a terminal or IDE terminal to run the Python script

## Get it running
### Creating a virtual environment
- Verify that either `pip` or `conda` exists on your system by running either `conda -V` or `pip -V`. If not, correct your Python installation.
- To create a virtual environment with pip follow these steps:
    - Install [virtualenv]() with the following command ```pip install virtualenv```
    - After it installs, run ```virtualenv <env_name>``` to create your virtual environment for this project. Replace <env_name> with any name of your choice
    - After the environment is created, run ```source <env_name>/bin/activate``` to activate your environment
- Once the environment is created, you should see your environment name as a prefix to your prompt in your terminal 

### Installing the required external modules
All the external modules required are present in the `requirements.txt` file. To install these required modules, follow these steps
- Open up a terminal in the root of the project
- Activate your environment by running ```source <env_name>/bin/activate```, like in the previous step
- Run ```pip install -r requirements.txt```
This should install all the required modules in your project environment.
Now you are all set to run the project!

### Running the shell
Sea Shell currently does not have a GUI of its own. It runs as a sub-shell of your existing shell in Linux, but supports all its commands independently.
- Open a terminal in the root of the project
- Run ```python3 shell.py``` to get Sea Shell running

If you have completed all the above steps successfully, then you should see a screen similar to the one below.

![](https://github.com/Parthiv-M/sea-shell/blob/master/extras/seashell-help.png)

Congratulations! You have successfully run the Sea Shell!

# Contributors
The Sea Shell was built by a team of four people including [Parthiv Menon](https://github.com/Parthiv-M), [Raghav Thakar](https://github.com/raghavthakar), [Jayant Shanmugam](https://github.com/Jayanth-Shanmugam), and [Ritika Tirumeni](https://github.com/RithikaThirumeni)
