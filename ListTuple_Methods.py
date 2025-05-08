a= input("Enter the elements with space: ") 
# if input is in list, it will treat it as string
print(list(a)) # turns each and every single item in 'a' into list
b= a.split() # splits the string by spaces and gives a list of strings.
print(b)
print(len(b))
c= list(map(int, a.split())) # map makes right according to left
# map right has to be list, tuple, dictionary or string(no spaces)
# map left is function which turns right according to left function
print(c)
d= b[0: len(b)-2] # sub array/list
"""print(d.sort())
print(d.reverse()) does not work as well as for others...Logical Error"""
d.sort() # sorts ascending order and original order is removed
# works for both tuple and list
print(d)
d.sort(reverse=True) # sorts in descending order and original order is removed
# works for both tuple and list
print(d)
d.reverse() # reverses the whole list and original order is removed
# works for both tuple and list
print(d)
e= input("Enter a tester: ")
d.append(e) # includes 'e' at last of list 'd'
print(d)
d.insert(0, e) # includes 'e' at left index
print(d)
d.pop(int(e)) # just deletes element at 'e' index
print(d)
print(d.pop(int(e))) # prints the element of 'e' index
d.remove(e) # removes first occurence of 'e' from d if found, else shows ValueError
print(d)
print(sum(c)) # sums all elements of list, tuple, dic (all have to be int)
print(max(d), min(d)) # gives the max and min element in list
# list can have list, dict, set as items
f= input("Enter the elements of tuple: ")
# if input is in tuple, it will treat it as string
print(tuple(f)) # turns each and every single item in 'f' into tuple
print(tuple(f.split())) # turns only elements as items of tuple, not spaces
# .split() will turn it into list and tuple() turns list into tuple
f= tuple(f.split())
print(f)
g= input("Enter the tester: ")
print(f.count(g)) # counts the no. of times 'g' appeared in 'f' tuple
print(max(f), "NEXT", min(f)) # gives the max and min element in tuple
print(f.index(g)) # gives the index of first appearance of 'g'
print(all(f)) # true if all elements are not 0, none, false
print(any(f)) # true if atleast 1 element is not 0, none, false
h= f # this works for both list and tuple
# But if i modify a list 'f', a list 'h' will also modify itself according to 'f'
# This issue not happens in tuple as they are immutable (permanant)
d= b.copy()
# This List issue can be solved using this as now i can modify 'd' and 'b' as i want
"""h= zip(h, f)
print(tuple(h))
print(list(h)) Doesn't work As after tuple(h), zip is exhausted i.e. Khatam"""
i= zip(h, f) # zip combines h and f equally
# (h and f can be both list or tuple or mix of both)
# REMEMBER:- zip works only 1 time i.e.
print(tuple(i))
# if you print tuple(i), zip is used up, nothing will be print like in """
i= zip(h, f)
# we need to again zip it up and use it. Simple :)
print(list(i))
print(sorted(f)) # creates new sorted ascending list, tuple and original is intact
print(list(reversed(f))) #  creates new reversed list, tuple and original is intact
print(sorted(f, reverse= True)) 
# creates new descending list, tuple and original is intact
# tuple can have list, dict, set as items
# tuple, though immutable, can have mutable items 
# e.g. if there is a list in tuple, the list can be updated