c=int(input("enter the current year:"))
f=int(input("enter the final year:"))
print("leap years are:")
for x in range(c,f+1):
    if(x%4==0 & x%100!=0)| (x%40==0):
        print(x)
    