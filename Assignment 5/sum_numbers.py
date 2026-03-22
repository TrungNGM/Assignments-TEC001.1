def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

input_numbers = input("Enter a list of numbers: ")
numbers = []
for i in input_numbers.split():
    numbers.append(int(i))
total = sum_numbers(numbers)
print("The sum of the numbers is:", total)
