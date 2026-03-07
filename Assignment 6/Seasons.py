seasons = ("Winter", "Spring", "Summer", "Autumn")
months = int(input("Enter the month number (1-12): "))
index = (months % 12) // 3
print("The season for month", months, "is:", seasons[index])