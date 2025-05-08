s1= input("Enter a sentence: ")
s2= input("Enter a sentence: ")
a= set(s1.split())
b= set(s2.split())
c= s1.split()
d= s2.split()
uni= a.symmetric_difference(b)
com= a.intersection(b)
d= {"uniques of sentence 1": a, "uniques of sentence 2": b,
    "commons": com, "uniques": uni}
print(d)