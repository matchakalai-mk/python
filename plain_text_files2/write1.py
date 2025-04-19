with open('poem.txt', 'w') as file:
    file.write('Roses are red,\n')
    file.write('Violets are blue,\n')
    file.write('Python is great,\n')
    file.write('And so are you.\n')

    file.writelines([
        'This is the first line.\n',
        'This is the second line.\n',
        'This is the third line.\n'
    ])


"""
    This script demonstrates how to write text to a file in Python using the `open` function.
    Functionality:
    - Opens a file named 'poem.txt' in write mode ('w'). If the file does not exist, it will be created.
    - Writes multiple lines of text to the file using the `write` method.
    - Appends additional lines of text to the file using the `writelines` method.
    Notes:
    - The `write` method writes a single string to the file.
    - The `writelines` method writes a list of strings to the file without adding newlines automatically.
    - The file is automatically closed after the `with` block is exited, ensuring proper resource management.
"""