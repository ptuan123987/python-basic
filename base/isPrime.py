import math


def main():
    try:
        number = int(input('Enter a number : '))
        is_check_prime = isPrime(number)
        print(is_check_prime)
        print_prime_number_less_num(number);
    except :
        print('Invalid')
    


def isPrime(num):
    if (num <= 0):
        return False
    for element in range(2, int(math.sqrt(num)+1) ):
        if (num % element == 0):
            return False
    return True
def print_prime_number_less_num(num) :
    count = 0;
    i=2;
    while(count < num) :
            if (isPrime(i)) :
                print(i);
                count+=1;
            i+=1;

main()
