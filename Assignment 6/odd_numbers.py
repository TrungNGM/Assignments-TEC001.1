def remove_odd_number (odds):
    result = []
    for number in odds:
        if number % 2 == 0:
            result.append(number)
    return result

input_numbers =(input("Enter a list of numbers: "))
numbers_list = []
for n in input_numbers.split():
    numbers_list.append(int(n))
new_list = remove_odd_number(numbers_list)

print("Original list: ", numbers_list)
print("List after removing odd numbers: ", new_list)