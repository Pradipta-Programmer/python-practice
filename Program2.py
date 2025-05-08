a= input("Enter the names with spaces: ")
l= a.split()
print(l)
t= ()
for i in range(0, len(l)):
    p= l[i]
    t= t + (p[0], )
print(t)
s= set(t)
print(s)