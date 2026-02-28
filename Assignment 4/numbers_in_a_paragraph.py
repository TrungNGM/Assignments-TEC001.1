import re
def sum_numbers_in_a_paragraph(text):
    numbers = re.findall('[0-9]+', text)
    total = 0
    for i in numbers:
        total += int(i)
    return total
        
while True:
    text = input('Enter a paragraph (enter nothing to stop):')
    if text == '':
       break
    print(sum_numbers_in_a_paragraph(text))
   