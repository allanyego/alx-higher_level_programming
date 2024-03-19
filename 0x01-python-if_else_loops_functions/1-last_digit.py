#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10 # abs ensures unsigned
print(f"Last digit of {number} is {last_digit} and " ,end='')
if last_digit == 0:
    print("is 0")
elif last_digit > 5:
    print("greater than 5")
else:
    print("is less than 6 and not 0")
