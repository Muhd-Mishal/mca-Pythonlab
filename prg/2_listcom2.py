n=int(input("enter the the limit"))
new=[]
for x in range(n):
    a=int(input("enter the numbers:"))
    new.append(a)
sqr=[x**2 for x in new]
print(sqr)