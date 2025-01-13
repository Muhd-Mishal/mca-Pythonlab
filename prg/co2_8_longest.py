n=int(input("enter the no of words:"))
l=[]
for i in range(n):
    x=input("enter a word:")
    l.append(x)
print(l)
max=len(l[0])
temp=l[0]
for i in l:
    if len(i)>max:
        max=len(i)
        temp=i
print("the word having longest length is ",temp,"and length is",max)