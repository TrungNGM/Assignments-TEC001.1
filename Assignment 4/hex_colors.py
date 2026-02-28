def valid_web_colors (colors):
    if len(colors) != 7:
        return False
    if not colors.startswith('#'):
        return False
    for i in colors[1:]:
        if not (i.isdigit() or i.upper() in 'ABCDEF'):
            return False
    return True

while True:
    colors = input('Enter Hex Color (enter nothing to stop): ')

    if colors == '':
        break

    if valid_web_colors(colors):
        print('True')
    else:
        print('False')