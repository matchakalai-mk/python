with open('poem.txt', 'a') as file:
    file.write('The Sun is bright,\n')
    file.write('The sky is blue,\n')
    file.write('The world is beautiful,\n')
    file.write('And so are you.\n')

    addditional_lines = [
        'This is the first line.\n',
        'This is the second line.\n',
        'This is the third line.\n'
    ]

    file.writelines(addditional_lines)

# 'a' mode is used to append text to the file without overwriting existing content.
# The file is opened in append mode, so any new content will be added to the end of the file.