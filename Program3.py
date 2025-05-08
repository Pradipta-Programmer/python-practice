l= int(input("Enter the number of students: "))
m= int(input("Enter the no. of subject marks: "))
d={}
for i in range(0, l):
    n= input("Enter the student name: ")
    d[n]= list(map(int, input(f"Enter the marks of {n}: ").split()))
s= list(d.values())
v= list(d.keys())
a= []
t= {}
y= 0
for i in range(0, m-1):
    a.append((sum(s[i]))/m)
for i in range(0, l):
    t[v[i]]= sum(s[y])
    y= y+1
p= []
for i in range(0, l):
    g= s[i]
    for j in range(0, m):
        if g[j] >= 40:
            y= 1
        else:
            y= 0
        if y==0:
            break
    if y== 1:
        p.append(v[i])
print("Passed students are: ", p)