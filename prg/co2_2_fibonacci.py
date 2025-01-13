first=0
second=1
l=int(input("enter the limit:"))
print("the fibonacci series of ",l,"is:")
print(first)
print(second)
for i in range(l-2):
    third=first+second
    first=second
    second=third
    print(third)
