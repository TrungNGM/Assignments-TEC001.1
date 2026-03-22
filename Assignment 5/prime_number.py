number = int(input("Enter a number: "))
for i in range (2, number):
    if number % i == 0:
        print(number, "is not a prime number.")
        break
else:
    if number > 1:
        print(number, "is a prime number.")
    else: 
        print(number, "is not a prime number.")