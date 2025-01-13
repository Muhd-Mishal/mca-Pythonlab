list=[]
sum=0
l=int(input("enter the limit:"))
print("enter ",l,"numbers:")
for i in range(l):
    x=int(input())
    list.append(x)
print(list)
for i in list:
    sum=sum+i
print("sum of list:",sum)