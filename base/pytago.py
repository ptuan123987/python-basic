import math;
def main():
    pass;
def pytago(n) :
    for i in range(1,n+1) : 
        for j in range(i+1,n+1):
            sum_square = i**2 + j**2;
            k = int(math.sqrt(sum_square));
            if((k **k) == sum_square and k < n) : 
                return i,j,k;
main();
print(pytago(5));   