n=int(input("enter the limit:"))
col=[]
for x in range(n):
    a=input("enter the color names:")
    col.append(a)
print(col)
print("the first color:",col[0])
print("the last color:",col[-1])
