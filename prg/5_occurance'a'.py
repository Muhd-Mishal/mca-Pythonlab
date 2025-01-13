l=int(input("enter the limit:"))
c=0
li=[]

for x in range(l):
    a=input("enter the names:")
    li.append(a)
for x in li:
    for j in x:
        if 'a' in j.lower():
            c+=1

print("occurrance of a :",c)