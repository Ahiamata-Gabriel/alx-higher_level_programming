#!/usr/bin/python3
number = 0
for i in range(0, 90):
    l_digit = number % 10
    f_digit = number // 10

    if (f_digit < l_digit and number < 89):
        print("{}{}".format(f_digit, l_digit), end=", ")
    elif (number == 89):
        print(89)
    number += 1
