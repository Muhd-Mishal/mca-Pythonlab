a=int(input("enter a number:"))
b=int(input("enter a number:"))
while b!=0:
    r=a%b
    a=b
    b=r
print("the gcd is:",a)