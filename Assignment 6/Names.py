names = set()
while True:
    name = input("Enter a name (Enter nothing to stop): ")
    if name == "":
        break
    elif name in names:
        print("Existing Name")
    else:
        print("New Name")
        names.add(name)
print ("\nNames entered:")
for i in names:
    print(i)