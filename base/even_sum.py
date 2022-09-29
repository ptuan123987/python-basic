def main():
    num = int(input('Enter number:'))
    sum = 0
    count = 0
    i = 0
    while (count < num):
        if (even_number(i)):
            print(i)
            count += 1
            sum += i
        i += 1
    print(f'Even sum less number : {sum}')
    pass


def even_number(num):
    if (num % 2 == 0):
        return True
    return False
main()
