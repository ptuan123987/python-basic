import math


def main():
    try:
        print('Print perfect number less than or equal n')
        num = int(input('Enter number : '))
        count = 0
        i = 0
        while (count < num):
            if (is_perfect_square(i)):
                print(i)
                count += 1
            i += 1
    except:
        print('Invalid Input')


def is_perfect_square(num):
    if (math.sqrt(num) == math.floor(math.sqrt(num))):
        return True
    return False


main()
