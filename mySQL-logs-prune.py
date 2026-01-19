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

print(f"Today is: {base_date}.")
# print(base_date)
# print(type(base_date))

# Lets go back 6 months plus one year
cut_date = base_date - timedelta(days=545)
print(f"Cut date is: {cut_date}.")

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
    dot_sql = file_name.endswith(".sql")
    if dot_sql:
        # This file qualifies so let's process it.
        #print(f"Good to process... {file_name}")
        # Extract the run date from the filename
        file_date = file_name[9:19]
        # print(file_date)
        # Split it into month day year
        temp_date = file_date.rsplit('-')
        # print(f" {temp_date} which is a {type(temp_date)}")
        
        # In case date doesn't parse correctly, skip
        if len(temp_date) < 3:
            continue
 
        # Turn that value into a data objext for comparison to cut_date
        run_date = date(int(temp_date[0]), int(temp_date[1]), int(temp_date[2]))
        # print(f"{run_date} which is a {type(run_date)}")

        # Compare against cut date
        if cut_date < run_date:
            print(f"Run date {run_date} is within Cut date {cut_date}.")
        else:
            print(f"File ({file_name}) is older than cut_date {cut_date}, it should be archived or deleted.")

    else:
        if file_name[0] == ".":
            continue
        else:
            print(f"Need to remove this file: {file_name}!!!!")
 

    # print(file_name + f" Exists: {exists(file_name)}, length: {len(file_name)} ")
    

# Delete a file
file = 'file1.txt'
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
path = os.path.join(location, file) 
# os.remove(path)

