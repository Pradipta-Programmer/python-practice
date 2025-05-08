s= input("Enter a sentence: ")
p= s.split()
d= {}
for i in range(0, len(p)):
    c= p.count(p[i])
    d[p[i]]= c
a= d.items()
d= dict(sorted(a, key= lambda item: item[1]))
print(d)