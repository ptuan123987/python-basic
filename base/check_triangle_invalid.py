def main():
    try: 
        print('Check Invalid Triangle   ')
        a_edge = float(input('Enter first edge : '));
        b_edge = float(input('Enter second edge : '));
        c_edge = float(input('Enter third edge : '));
        if(a_edge > 0 and b_edge > 0 and c_edge>0) :
            check = is_triangle(a_edge,b_edge,c_edge);
        print(check);
    except :
        print('Invalid')
   

def is_triangle(a_edge, b_edge, c_edge):
    if (a_edge + b_edge <= c_edge and a_edge + c_edge <= b_edge and b_edge + c_edge <= a_edge):
        return False;
    return True;
main()
    
