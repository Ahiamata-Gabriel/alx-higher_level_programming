#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last_num = number % 10
if (number < 0):
    number *= -1
    last_num = number % 10
    last_num *= -1
    number *= -1
if (last_num > 5):
    print("{} {} is {} and is greater than 5".format(str, number, last_num))
elif (last_num == 0):
    print("{} {} is {} and is 0".format(str, number, last_num))
elif (last_num < 6 and last_num != 0):
    print(f"{str} {number} is {last_num} and is less than 6 and not 0")
