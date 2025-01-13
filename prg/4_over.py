l=int(input("enter the limit:"))
list=[]
for x in range (l):
    a=int(input("enter the numbers"))
    if a > 100:
        list.append("over")
    else:
        list.append(a)
print(list)