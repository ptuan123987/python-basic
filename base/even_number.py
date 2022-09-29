def main():
    num = int(input('Enter number : '))
    count = 0
    i = 0
    while (count < num):
        if (even_number(i)):
            count += 1
            print(i)
        i += 1


def even_number(num):
    if (num % 2 == 0):
        return True
    return False


main()
