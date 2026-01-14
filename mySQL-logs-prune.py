import os 
from sys import argv

script, log_path = argv


dir_list = os.listdir(log_path) 
print("Files and directories in '", log_path, "' :") 
print(dir_list)