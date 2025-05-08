a= input("Enter the name: ")
print("Good Afternoon ", a)
print(f"Good Afternoon {a} Boss") # f allows to put {} in ""
print(sorted(a)) # sorts string in ascending
print(sorted(a, reverse=True)) # sorts string in descending
n= a[0: len(a)] # 0 te start and len diye last porjonto print
print(n)
n= a[: len(a)-1]  # left always included: right last index not included
print(n)
n= a[0:] # nothing means from beginning (left): nothing means to the last (right)
print(n)
n= a[1:5:2] # left : middle takes substring, then right decides gaps/skips in sub
print(n) # first letter of sub is put then from next letter count and 
# when count ends, the count ended number is put there and repeat
print(a[::-2]) # negative makes it go from back, thus reversing the string
# negative makes only go from back, the number is doing the work of right
# think of only the number, not -
b= input("Enter a sentence: ")
c= input("Enter the tester: ")
print(b.startswith(c))# checks start of b and gives true false if 'c' is in end of b
print(b.endswith(c)) # checks last of b and gives true false if 'c' is in end of 'b' 
print(b.count(c)) # counts no. of items of 'c' in 'b'
print(b.capitalize()) # capitals the first letter of 'b'
print(b.find(c)) # gives the position of 'c' in 'b' for the first time appearance
# gives -1 if not found
print(b.isdigit()) # checks if all of 'b' is digit 
print(b.isalpha()) # checks if all of 'b' is letters 
print(b.replace("a", c)) # replace the first with the second
print(b.replace("c", c).replace("o", c)) # 2 replaces occur. More can be done
# above technique of 2 or more replaces not works in others
print(b.title()) # capitalises first letter of each word of sentence
print(b.upper(), "\n", b.lower()) # UpperCase and LowerCase
print(b.strip()) # removes spaces like .trim
print(b.lstrip(), "NEXT", b.rstrip()) # trims left and right of 'b' respectively
print(b.rfind(c)) # finds last index of c in b
print(b.index(c)) # gives the position of 'c' in 'b' for the first time appearance
# gives error if not found
print(b.isnumeric()) # checks if all elements are numbers or not
print(b.isalnum()) # checks if every element is either number or alphabet or not
print(b.join(a)) # joins 2 strings together in a peculiar way
# if 'a' is 1 character string, a in first joined with b
# if 'a' is more than 1 character string, each character of a will join b one by one
d= "1"
print(d.zfill(3)) # attaches 0 in left of a fully numberic string (og is unchanged)
# total length of the new string is 3 so accordingly add 0
print(d.ljust(5, "p")) # adds bracket's right to d's right
print(d.rjust(5, "p")) # adds bracket's right to d's left