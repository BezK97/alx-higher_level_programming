#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    size = len(argv) - 1
    operator = ['+', '-', '*', '/']
    a = 0
    b = 0
    result = 0

    if size != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        for i in range(len(operator)):
            if argv[2] != operator[i] and i != 3:
                continue
            elif argv[2] != operator[i] and i == 3:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
            else:
                a = int(argv[1])
                b = int(argv[3])
                if i == 0:
                    result = add(a, b)
                elif i == 1:
                    result = sub(a, b)
                elif i == 2:
                    result = mul(a, b)
                else:
                    result = div(a, b)
                print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, result))
                exit(0)
