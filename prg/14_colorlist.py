a=['green','blue','yellow']
b=['red','blue']
print(a)
print(b)
for x in range(len(a)):
    if a[x] not in b:
        print("the color is :",a[x])