import random

random_num = random.randint(1, 10)
while True:
    guess = (float(input('Enter your number between 1 and 10 (enter nothing to stop):')))

    if guess > random_num:
        print('Too high')
    elif guess < random_num:
        print('Too low')
    else:
        print('Correct')
        break
print('thanks for playing :)')
