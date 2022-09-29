import math


def main():

    pass


def expr(x, n):
    expr_x = 0
    p = 0
    for i in range(0, n+1):
        p = (x**i) / factorial(i)
        expr_x += p
    return expr_x

def factorial(x):
    result = 1
    for i in range(1, x+1):
        result = result * i
    return result

print(expr(2,1000));

main()
