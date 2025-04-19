# Open the file 'jokes.txt' in read mode using a raw string for the file path
# and the 'with' statement to ensure proper resource management.
# The 'with' statement automatically closes the file after the block is executed, even if an error occurs.
with open(r'jokes.txt', 'r') as file:

    # Read all lines from the file into a list
    lines = file.readlines()

    # Check if the file has at least 10 lines; if so, get the 10th line (index 9), otherwise set a default message
    content = lines[9] if len(lines) > 9 else "Line 10 does not exist."

    # Print the content of the 10th line or the default message
    print(content)

# The file is automatically closed after the 'with' block, ensuring that system resources are freed up.

### Exercise: ###
# Play with loops and conditions to read the file line by line.
# For example, you can read the first 5 lines of the file and print them one by one.
# You can also use a for loop to iterate through the lines in the file and print them.