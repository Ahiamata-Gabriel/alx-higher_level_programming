#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    for n in range(len(sys.argv) - 1):
        sum = sum + int(sys.argv[n + 1])
    print(sum)
