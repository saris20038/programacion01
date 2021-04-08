print("LAST POINT", '#'*70) 

Position= int(input("tell a position for the fibonacci ecuation: "))
def FIBONACCI (n):
    if n < 2:
        return n 
    else:
        print((n-1)+(n-2))


FIBONACCI(Position)