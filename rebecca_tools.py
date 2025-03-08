import os

# Read docs/tools.md to know how to create your tools.

def terminal(command: str):
    """
    Run a command in the terminal.
    """
    while True:
        print(f"\n\nAssistant is using command {command}. Accept it? (Y or N)")
        thing = input(">").lower()
        if thing == "n":
            return "Could not run command."
        elif thing == "y":
                return os.popen(command).read()
        else:
            print("Invalid input. Try again.")

def write_file(path: str, content: str):
    """
    Write content to a file. Creates a file with the content if the file doesn't exists.
    """
    with open(path, "w") as f:
        f.write(content)
        
    return "File " + path + " Created"

def read_file(path: str):
    """
    Reads a file
    """
    with open(path, "r") as f:
        return f.read()
    
def delete_file(path: str):
    """
    Deletes a file
    """
    os.remove(path)
    return "File " + path + " removed."
    
def list_files(path: str):
    """
    List files in a directory
    """
    return os.listdir(path)

def get_current_directory():
    """
    Gets the current directory
    """
    return os.getcwd()

def change_directory(path: str):
    """
    Changes the current directory
    """
    os.chdir(path)
    return "Changed directory to "+path
    
tools = [write_file, read_file, list_files, get_current_directory, change_directory]