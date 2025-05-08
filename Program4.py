l= int(input("Enter the number of strings: "))
s= []
for i in range(0, l):
    s.append(input("Enter the string: "))
f= []
g= []
for i in range(0, l):
    p= s[i]
    q= p[::-1]
    if p==q:
        f.append(p)
    else:
        g.append(p)
f= tuple(f)
g= tuple(g)
print(f)
print(g)