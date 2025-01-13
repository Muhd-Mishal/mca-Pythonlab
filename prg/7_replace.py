n=input("enter a text")
b=n[0]
s=n[1:len(n)]
for i in range(len(s)):
    if s[i]==n[0]:
        b=b+"$"
    else:
        b=b+s[i]
print(b)