num=[2,3,7,3]
num2=[1,2,3,4,5]

print(len(num))
print(len(num2))
if len(num) == len(num2):
    print("it has same length")
else:
    print("it doesnt have same length:")

print("sum of num:",sum(num))
print("sum of num2:",sum(num2))

if sum(num)==sum(num2):
    print("it has same sum")
else:
    print("it has different sum")
    
print("the common elements are:")
for i in num:
    for j in num2:
        if i == j:
            print(i)