import math
def main():
    pass

def dec_to_binary(x):
    result = [];
    while(x != 0 ) :
        num = x %2 ;
        result.append(num);
        x =int(x/2);
    result.reverse();
    return result;
print(dec_to_binary(6));

main()
