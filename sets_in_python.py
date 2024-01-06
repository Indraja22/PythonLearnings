# Set is an unorderd collection with no duplicate items
baskets = {"oranges","apples","oranges","cherry","pear"}
print(baskets) # duplicates were removed
print(set(baskets))
print(set("abracadabra"))
ispresent = 'oranges' in baskets
print(ispresent)
a = set("abracadabra")
print(a)
b = set("alacazam")
print(b)
print(a - b) # items in a but not in b
print(b - a) # items in b but not in a
print(a | b) # all items in a and b
print(a & b) # only common items in a and b
print(a ^ b) # exclude common letter in a and b

# Set Comprehensions
d = {x for x in 'abracadabra' if x not in 'abc'}
print(d)
