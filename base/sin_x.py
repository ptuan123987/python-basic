import math


def main():
    pass


def sin(x, n):
    sin_x = 0
    p = 0
    for i in range(1, n+2):
        p = float((-1)**(i-1) * (x**(2*i-1))/(factorial(2*i-1)))
        sin_x += p
    return sin_x


def factorial(x):
    factorial_x = 1
    for i in range(1, x+1):
        factorial_x = factorial_x * i
    return factorial_x

print(sin(math.pi /2,100));
main()
