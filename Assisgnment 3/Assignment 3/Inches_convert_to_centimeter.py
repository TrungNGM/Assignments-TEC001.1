x = float(input('Enter a number in inches (negative number to stop):'))


while x >= 0:
    y = x * 2.54
    print(x, '(inches) = ', y, '(cm)' )

    x = float(input('Enter a number in inches (negative number to stop):'))
print('bye')

