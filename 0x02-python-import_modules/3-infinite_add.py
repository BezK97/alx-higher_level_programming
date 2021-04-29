#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    size = len(argv) - 1
    result = 0

    if size == 0:
        print(result)
    else:
        for i in range(1, size + 1):
            result += int(argv[i])
        print(result)
