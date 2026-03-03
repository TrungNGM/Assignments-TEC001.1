smallest = None
largest = None

while True:
    Input = input('enter a number (enter nothing to stop):')
    if Input == '':
        break
    num = float(Input)

    if smallest is None or num < smallest:
        smallest = num

    if largest is None or num > largest:
        largest = num

if smallest is not None:
        print("Smallest number:", smallest)
        print("Largest number:", largest)
else:
        print('bye')
