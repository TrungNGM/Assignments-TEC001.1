numbers = []
while True:
    input_number = input("Enter a number (Enter nothing to stop): ")
    if input_number == "":
        break
    numbers.append(int(input_number))
numbers.sort(reverse=True)
print("Five greatest numbers in descending order:")
for num in numbers[:5]:
    print(num)