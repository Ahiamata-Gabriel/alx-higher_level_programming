#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
last_num_str = num_str[-1]
last_num = int(last_num_str)
str = "Last digit of {} is {}".format(number, last_num)
if last_num > 5:
    print("{} and is greater than 5".format(str))
elif last_num == 0:
    print("{} and is 0".format(str))
elif last_num < 6 != 0:
    print("{} and is less than 6 and not 0".format(str))