import re

def hide_phone_numbers(text):
    pattern = r'\b\d{10}\b|\+84\d{9}\b'
    
    return re.sub(pattern, '[REDACTED]', text)

while True:
    text = input('Enter text (press Enter to stop): ')
    if text == '':
        break
    print(hide_phone_numbers(text))