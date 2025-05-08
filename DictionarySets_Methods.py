d= dict(abc=1, de=2, ghi=3, jkl=4, mno=5) # changes this into dict
# for user input, we need looping
# Alternatively, we can use d.update({key: value})
# normal dict looks like this {"abc": 1, "def": 2, "ghi": 3, "jkl": 4, "mno": 5}
print(d)
a= dict((["opq", 1], ["rst", 2], ["uvw", 3], ["xyz", 4]))
# this works too. Any Combination of List and Tuple both will be fine
print(a)
# len works here too. Not Writing it :)
b= input("Enter tester: ")
print(d[b]) # gives the corresponding value of the key if found, else ERROR
print(d.get(b, "NOT FOUND")) # gives the corresponding value of the key or else right
print(d.keys(), "\n", d.values(), "\n", d.items())
# gives keys, values, items respectively
d= {**d, **a} # unpacks two dicts into one
d.update(a) # Same
# in both 2 cases, same key is ignored, unless there is any change in value
e= d | a # Copies d and a in e
f= dict(zip(d, a)) # You know what's going on
print(d, "\n", e, "\n", d, "\n", f)
print(d.pop(b, "NOT FOUND")) # Permanent removal of b from d and give it as result
print(d.popitem()) # Permanent removal of last item from d and give it as result
print(d)
c= input("Enter another tester: ")
print(b in d) # checks if b is in d
e= d.copy() # copies
d= dict.fromkeys([b, c], 9) # deletes and creates new dict with keys:values{b:9, c:9}
print(d)
del d[b] # deletes d[b] if available or Error
print(d)
print(d.setdefault(c, "10")) # returns value of key c if found, else add {c: 10}
print(dict.fromkeys(d, 0)) # changes values of keys of d to 0
print(d.clear()) # completely clears d
# dict can never have list, dict, set as key 
# but can put tuple as key since tuple is immutable
# they can be put as value though
# Remember:-tuple as key can only be possible if it has immutable items like int,str 
s1= set(input("Enter set elements: ")) # coverts each and every input into set items
# set takes input at random position and no duplicate element can stay in set(1 only)
print(s1)
t= input("Enter a tester: ")
s1.add(t) # adds t to s1  (t is added as a single item)
print(s1)
s1.update(t, "ijk") # works same like .add() but multiple text/items can be added
# all items in bracket are separated from each other and added to s1
print(s1)
s1.remove(t) # Removes the element — shows error if not present
s1.discard(t) # Removes the element — not shows error if not present
# same functions repeats pop(), clear(), copy()
s2= set(input("Enter another set elements: "))
s3= s1.union(s2) # union ( U ) like in set
# shortcut for union()=> s1 | s2
print(s3)
s3= s1.intersection(s2) # intersection ( ∩ ) like in set
# shortcut for intersection()=> s1 & s2
print(s3)
s3= s1.difference(s2) # s1-s2 like in set
# shortcut for difference()=> s1-s2
print(s3)
s3= s1.symmetric_difference(s2) #removes same terms but includes unique terms of both
# shortcut for symmetric difference()=> s1 ^ s2
# above 4 creates new set with the functions but original is unchanged
s1.intersection_update(s2) # s1 ∩ s2 but new set is put in s1
# shortcut for intersection update()=> s1 &= s2
s1.difference_update(s2) # s1-s2 but new set is put in s1
# shortcut for difference update()=> s1-=s2
s1.symmetric_difference_update(s2)
# shortcut for symmetric difference()=> s1 ^= s2
# removes same terms but includes unique terms of both and put it in s1
# above 3 changes s1 with the functions
print(s1.issubset(s2)) # True if all elements of a in b
# shortcut for subset()=> s1 <= s2
print(s1.issuperset(s2)) # True if all elements of b in a
# shortcut for subset()=> s1 >= s2
print(s1.isdisjoint(s2)) # True if a and b have no common elements
print(s1 < s2) # Proper Subset
# True if all terms of s1 is in s2 but s1 is != to s2 (s1 has fewer terms) 
print(s1 > s2) # Proper Superset
# True if all terms of s2 is in s1 but s2 is != to s1 (s2 has fewer terms)
print(s1 == s2) # True if terms of s1 is same as terms of s2
# set can never have list, dict, set but can put tuple since tuple is immutable
# but also tuple can't have any mutable item in it
# Remember:-tuple can only be possible if it has immutable items like int,str