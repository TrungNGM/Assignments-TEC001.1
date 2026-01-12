import random

code_3_digit = [random.randint(0, 9) for _ in range(3)]
code_4_digit = [random.randint(1, 6) for _ in range(4)]

print("3-digit code:", code_3_digit)
print("4-digit code:", code_4_digit)