
def unit_price(diameter_cm, price):
    radius_m = (diameter_cm / 2) / 100
    area = 3.14 * radius_m ** 2
    return price/area


d1 = int(input("Enter diameter of first pizza (cm): "))
p1 = int(input("Enter price of first pizza (USD): "))

d2 = int(input("Enter diameter of second pizza (cm): "))
p2 = int(input("Enter price of second pizza (USD): "))

u1 = unit_price(d1, p1)
u2 = unit_price(d2, p2)

if u1 < u2:
    print("First pizza is better value.")
elif u2 < u1:
    print("Second pizza is better value.")
else:
    print("Both pizzas have the same value.")
