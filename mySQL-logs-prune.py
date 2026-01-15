import os 
from sys import argv
from os.path import exists
from datetime import date, datetime, timedelta

script, log_path = argv

# Change current directory
def current_path(): 
    print("Current working directory") 
    print(os.getcwd()) 
    print() 

current_path() 
os.chdir(log_path) 
current_path()

# In the directory where the files are in.
#
# Here goes some date arithmetic

date_format = "%Y-%m-%d"
base_date = date.today()

print(f"Today is: {base_date}")
print(base_date)
print(type(base_date))

# Lets go back 6 months plus one year
cut_date = base_date - timedelta(days=365)
print(cut_date)

# Let's build the filename to compare against

string_cut_date = cut_date.strftime(date_format)
cut_filename = "Node-Red_" + string_cut_date + ".sql"
print(f"Cut filename: {cut_filename}")


# Done with filename build

# Time to go get files in the directory
#
# List contents of a direcory
dir_list = os.listdir(log_path) 
print("Files and directories in '", log_path, "' :") 

# Let's check to see if each log file is within the within the last 6 months
for file_name in dir_list:
    print(file_name + f" Exists: {exists(file_name)}, length: {len(file_name)} ")
    pass  # needed since I commented out the above line.


# Delete a file
file = 'file1.txt'
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
path = os.path.join(location, file) 
# os.remove(path)

