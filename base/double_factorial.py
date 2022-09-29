def main():
    try:
        num = int(input('Enter number:'))
        if (num >= 0):
            print(double_factorial(num))
    except:
        print('Invalid')


def double_factorial(num):
    if (num == 1 or num == 2):
        return num
    return num * double_factorial(num-2)


main()
