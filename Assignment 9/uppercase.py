def convert_uppercase(filename):
    with open (filename, 'r') as infile:
        content = infile.read()
    content = content.upper()
    with open ('output.txt', 'w') as outfile:
        outfile.write(content)

convert_uppercase("input.txt")