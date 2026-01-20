a = input("your biological sex (male or female): ")
b = float(input("your hemoglobin value (g/l): "))

if a == "male":
    if b < 117:
        print ("your hemoglobin value is low")
    elif b <= 155:
        print("your hemoglobin value is normal")
    else:
        print("your hemoglobin value is high")

elif a == "female":
    if b < 134:
        print ("your hemoglobin value is low")
    elif b <= 167:
        print("your hemoglobin value is normal")
    else:
        print("your hemoglobin value is high")

else:
    print("invalid sex, please rewrite")

