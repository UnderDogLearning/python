#5 Different ways to read a file line by line in Python
-------------------------------------------------------
#Open file    
fileHandler = open ("data.txt", "r")
# Get list of all lines in file
listOfLines = fileHandler.readlines()
# Close file
fileHandler.close()

# Iterate over the lines, strip() is used to the empty lines inbetween the lines
for line in listOfLines:
    print(line.strip())
   
#But if file size is large then it will consume a lot of memory, so better avoid this solution in case of large files

#Read a file line by line using readline()

# Open file        
fileHandler = open ("data.txt", "r")
while True:
    # Get next line from file
    line = fileHandler.readline()
    # If line is empty then end of file reached
    if not line :
        break;
    print(line.strip())
# Close Close    
fileHandler.close()


# Open file
with open ("data.txt", "r") as fileHandler:
    # Read each line in loop
    for line in fileHandler:
        # As each line (except last one) will contain new line character, so strip that
        print(line.strip())
       
# open a file
file_object = open('sample.txt')
# read the file content
data = file_object.read()
# print file content
print(data)
#close the file
file_object.close()

#we don’t call the close() function, then its object will be consuming the memory of our process. Also, there might be chances that data will not entirely be flushed to the file.


# File is not closed in case of exception
try:
    # open a file
    file_object = open('sample.txt')
    # read file content
    data = file_object.read()
    # It will raise an exception
    x = 1 / 0
    print(data)
    file_object.close()
except:
    # Handling the exception
    print('An Error')
finally:
    if file_object.closed == False:
        print('File is not closed')
    else:
        print('File is closed')


# using "with statement" with open() function, we dont need to use the close() function to close the file
with open('sample.txt', "r") as file_object:
    # read file content
    data = file_object.read()
    # print file contents
    print(data)
# Check if file is closed
if file_object.closed == False:
    print('File is not closed')
else:
    print('File is closed')
   
#“with statement” creates an execution block and object created in the with statement will be destroyed or gracefully closed when this execution block ends.


#Open multiple files in a single “with statement”

# Read from sample.txt and write in outfile.txt
with open('outfile.txt', 'w') as file_obj_2, open('sample.txt', 'r') as file_obj_1:
    data = file_obj_1.read()
    file_obj_2.write(data)
    # Both the files will be closed automatically when execution block ends.
   
   
# Check if the string exists in a file
def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False

# Check if string 'is' is found in file 'sample.txt'
if check_if_string_in_file('sample.txt', 'is'):
    print('Yes, string found in file')
else:
    print('String not found in file')


#Search for a string in file & get all lines containing the string along with line numbers

def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results


matched_lines = search_string_in_file('sample.txt', 'is')
print('Total Matched lines : ', len(matched_lines))
for elem in matched_lines:
    print('Line Number = ', elem[0], ' :: Line = ', elem[1])
   
   
   
#Search for multiple strings in a file and get lines containing string along with line numbers
def search_multiple_strings_in_file(file_name, list_of_strings):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results
   
# search for given strings in the file 'sample.txt'
matched_lines = search_multiple_strings_in_file('sample.txt', ['is', 'what'])
print('Total Matched lines : ', len(matched_lines))
for elem in matched_lines:
    print('Word = ', elem[0], ' :: Line Number = ', elem[1], ' :: Line = ', elem[2])
    
    
#remove a file 


import os
# Remove a file
os.remove('/home/somedir/Documents/python/logs')


#Remove a file if exists using os.remove()
import os
filePath = '/home/somedir/Documents/python/logs';
# As file at filePath is deleted now, so we should check if file exists or not not before deleting them
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")

#similar to os.remove we os module has another function that's os.ulink

import os 
# Handle errors while calling os.ulink()
try:
    os.ulink(filePath)
except:
    print("Error while deleting file ", filePath)


#Check if a file is empty using os.stat() in Python

import os
file_path = 'mysample.txt'
# check if size of file is 0
if os.stat(file_path).st_size == 0:
    print('File is empty')
else:
    print('File is not empty')



# other method of checking the file size 

import os
file_path = 'mysample.txt'
if os.path.getsize(file_path) == 0:
    print('File is empty')
else:
    print('File is not empty')
    
    
#First check if the file exists or not 

import os
def is_file_empty(file_path):
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0
    
file_path = 'mysample.txt'

is_empty = is_file_empty(file_path)

if is_empty:
    print('File is empty')
else:
    print('File is not empty')

# or 

#First check if the file exists or not 

import os
def is_file_empty(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) == 0
    
file_path = 'mysample.txt'

is_empty = is_file_empty(file_path)

if is_empty:
    print('File is empty')
else:
    print('File is not empty')
    
    

# Get Last Modification date & time of a file.

#os.path.getmtime(path)
import os
import stat
import time
import datetime

modTimesinceEpoc = os.path.getmtime(filePath)
modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
print("Last Modified Time : ", modificationTime )


#Otherway get time modified the file
# Convert seconds since epoch to Date only
modTimesinceEpoc = os.path.getmtime(filePath)
modificationTime = time.strftime('%d/%m/%Y', time.localtime(modTimesinceEpoc))
print("Last Modified Time : ", modificationTime )

#otherway Get time modified the file
modTimesinceEpoc = os.path.getmtime(filePath)
modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
print("Last Modified Time : ", modificationTime )

#Time in UTC time
modTimesinceEpoc = os.path.getmtime(filePath)
modificationTime = datetime.datetime.utcfromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
print("Last Modified Time : ", modificationTime , ' UTC')


#Append text or lines to a file

# Open a file with access mode 'a'
file_object = open('sample.txt', 'a')
# Append 'hello' at the end of file
file_object.write('hello')
# Close the file
file_object.close()


#Append a text to file in Python using ‘with open’ statement
with open('sample.txt', 'a') as file_object:
    file_object.write("hello")
    
#Append data to a file as a new line

# Open the file in append & read mode ('a+')
with open("sample2.txt", "a+") as file_object:
    # Move read cursor to the start of file.
    file_object.seek(0)
    # If file is not empty then append '\n'
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    # Append text at the end of file
    file_object.write("hello hi")
    
    
#append in function:

def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)
        
       
#Add a column to an existing CSV file

