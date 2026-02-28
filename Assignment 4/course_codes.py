def code_is_valid (code):
    if len(code) != 6:
        return False
    if not code[:3].isupper() or not code[:3].isalpha():
        return False
    if not code[3:].isdigit():
        return False
    return True

while True:
    code = input('Enter Your Course Code(enter nothing to stop):')

    if code == '':
        break

    if code_is_valid(code):
        print('True')
    else:
        print('False')