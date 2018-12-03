import math
def no_of_factors(a):
    c=0
    for i in range(1,math.ceil(a/2)):
        if a%i==0:
            c+=1
    return c
n=int(input("Enter a number: "))
if no_of_factors(n)==1:
    print(str(n) + " is a prime number.")
else:
    print(str(n) + " is not a prime number.")
