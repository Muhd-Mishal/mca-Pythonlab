n=int(input("enter the no of rows"))
for i in range(1,n):
    for j in range(i):
        print("*",end='')
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()
    