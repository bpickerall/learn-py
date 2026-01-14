import os 
from sys import argv
from os.path import exists
from datetime import date
script, log_path = argv

# Change current directory
def current_path(): 
    print("Current working directory") 
    print(os.getcwd()) 
    print() 

current_path() 
os.chdir(log_path) 
current_path()

t = date.today()
print(f"Today is: {t}")


# List contents of a direcory
dir_list = os.listdir(log_path) 
print("Files and directories in '", log_path, "' :") 

for file_name in dir_list:
    # print(file_name + f" Exists: {exists(file_name)}, length: {len(file_name)} ")
    pass


# Delete a file
file = 'file1.txt'
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
path = os.path.join(location, file) 
# os.remove(path)

