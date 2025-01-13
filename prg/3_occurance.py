w=input("enter a text:")
c=dict()
words=w.split()
for x in words:
    if x in c:
        c[x]+=1
    else:
        c[x]=1
print(c)