#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    size = len(argv) - 1

    if size == 0:
        print("{:d} arguments.".format(size))
    elif size == 1:
        print("{:d} argument:".format(size))
    else:
        print("{:d} arguments:".format(size))
    for i in range(1, size + 1):
        print("{:d}: {:s}".format(i, argv[i]))
