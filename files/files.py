# Reading a files contents - open(path_to_file, mode)
# mode = a - appending txt, w - writing txt, r - reading text
# myFile = open('./files/myFile.txt', 'r')

with open('./files/myFile.txt', 'r') as f:
# Read file
    # contents = f.read()
    # print(contents)
# returns the file contents as a list of strings
    # [print(line) for line in f.readlines()]
# remove the blank line
    [print(line.strip()) for line in f.readlines()]
f.close()

# read the text file line by line
with open('./files/myFile.txt', 'r') as f:
   for line in f:
        print(line.strip())
# Must close file or it will remain open 
f.close()

# Writing/appending to file - if the file passed doesn't exist the open() call will create the file (Error if the directory is not found)
lines = ['Readme', 'How to write text files in Python']
with open('./files/myFile.txt', 'a') as f:
    for line in lines:
        f.write('\n')
        f.write(line)
        f.write('\n')
f.close()

with open('./files/myFile.txt', 'r') as f:
    [print(line.strip()) for line in f.readlines()]
f.close()

# Import to check if the file exists or not
from os.path import exists as file_exists

file_exists = file_exists('./files/myFile.txt')

print(file_exists)

# Checking if exists with pathlib import
from pathlib import Path as file_exists

path_to_file = './files/myFile.txt'
file_exists = file_exists(path_to_file)

if file_exists.is_file():
    print(f'The file {path_to_file} exists')
else:
    print(f'The file {path_to_file} does not exist')