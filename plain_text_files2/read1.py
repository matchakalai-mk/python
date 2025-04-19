# Open the file in read mode. 'r' refers to read mode
file = open(r'jokes.txt', 'r') # open() returns a file object

# Read the file content, which is a string
content = file.read()

# Print the content of the file
print(content)

# The file is closed after reading to ensure that system resources are freed up.
file.close() 



### Notes: ###
# The program uses Python's built-in open() function, 
# which is part of Python's standard library, to read the text file. 
# No external library is used in this code.
###
