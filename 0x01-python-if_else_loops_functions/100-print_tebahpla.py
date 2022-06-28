#!/usr/bin/python3
for l in range(ord("z"), ord("a") - 1, -1):
    print("{}".format(chr(l - (32 if l % 2 == 1 else 0))), end="")
