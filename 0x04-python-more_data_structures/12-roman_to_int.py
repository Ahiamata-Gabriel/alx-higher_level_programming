#!/usr/bin/python3


def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    dict_r = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    int_value = 0

    for i in range(len(roman_string)):
        if dict_r.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                dict_r[roman_string[i]] < dict_r[roman_string[i + 1]]):
                int_value += dict_r[roman_string[i]] * -1

        else:
            int_value += dict_r[roman_string[i]]
    return (int_value)
