def main():
    pass


def cos_x(x, n):
    cos_x = 0
    p = 0
    for i in range(0, n+1):
        p = ((-1)**i)*(x**i)/factorial(2*i)
        cos_x += p

    return cos_x


def factorial(x):
    factorial_x = 1
    for i in range(1, x+1):
        factorial_x = factorial_x * i
    return factorial_x
