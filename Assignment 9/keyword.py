def count_keywords(filename, keyword):
    lines = []
    
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                lines.append(i)
    return lines
print(count_keywords("input.txt", "Python"))