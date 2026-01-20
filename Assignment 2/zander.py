a = float(input("length of zander in centimeters:"))

if a < 42:
    print("the zander doesn't meet the limit, please release the fish back into the lake")
    print("the size of the current Zander below the size limit is:", 42 - a)
else:
    print("the zander meets the size limit")