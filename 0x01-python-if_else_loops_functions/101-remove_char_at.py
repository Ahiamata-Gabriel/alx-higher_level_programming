#!/usr/bin/python3
# Creates a copy of str and removes the character at n.


def remove_char_at(str, n):
    return (str[0:n] + str[n+1:] if n >= 0 else str)
