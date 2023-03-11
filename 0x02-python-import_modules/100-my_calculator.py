#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    argv_count = len(argv)
    operators = ["+", "-", "*", "/"]
    if argv_count is not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        ops = sys.argv[2]
        if ops is "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif ops is "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif ops is "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif ops is "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
