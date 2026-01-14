from sys import argv

input_file = ex20_test.txt

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line