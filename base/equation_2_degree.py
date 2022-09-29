import math


def main():
    
    try:
        a = float(input('Enter a : '))
        b = float(input('Enter b : '))
        c = float(input('Enter c : '))
        if (a == 0):
            # the equation 1 degree
            equation_1_degree(b, c)
        else:
            # the equation 2 degree
            equation_2_degree(a, b, c)
    except:
        print('Invalid')


def equation_1_degree(b, c):
    if (b == 0):
        if (c == 0):
            print('Infinitely solutions')
        else:
            print('the equation no solution')
    else:
        result = -b/c
        print(f"the equation has 1 solution {result}")


def equation_2_degree(a, b, c):
    delta = b**2 - 4*a*c
    if (delta == 0):
        result = -b/2*a
        print(f'the equation has 1 solution {result}')
    elif (delta > 0):
        result_1 = -(b+math.sqrt(delta))/2*a
        result_2 = -(b-math.sqrt(delta))/2*a
        print(f'the equation has 2 solution {result_1} and {result_2} ')
    else:
        print('the equation no solution')


main()
