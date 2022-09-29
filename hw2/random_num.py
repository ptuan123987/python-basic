import random


def main():
    num = int(input("Enter number : "));
    numbers = []
    count = 0;
    while(count < num) :
        numbers.append(random.randint(0,num));
        count += 1;
    print(numbers);
    print(max(numbers));
    print(min(numbers));
    print(most_common(numbers));
    
def most_common(list):
    counter = 0 ; 
    num = list[0] ;
    for i in list : 
        cur_frequency = list.count(i);
        if(cur_frequency > counter ) :
            counter = cur_frequency;
            num = i;
    return num,counter;
main();