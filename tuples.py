# making a tuple
# tuple is ordered and unchangeable
dimensions = (1920, 1080)
print(dimensions)
print(dimensions.index(1920))

# duplicate items
fruits = ("apple", "cherry", "apple", "mango")
print(fruits)

# create tuple with one item
thistuple = ("apple",)
print(type(thistuple))

# Not a tuple
thistuple = ("apple")
print(type(thistuple))

# tuple() constructor
mytuple = tuple(("monsoon", "summers", "winter"))
print(type(mytuple))
print(mytuple)

# multiply tuples
newtuple = mytuple * 2
print(newtuple)

# join tuples
tuple1 = (1, 2, 3)
tuple2 = (12, 22, 23)
jointuple = tuple1 + tuple2
print(jointuple)

# loop through tuples
fruit_basket1 = ("chickoo", "kiwi", "oranges")
fruit_basket2 = ("guava", "mangoe", "strawberry")
for fruit in fruit_basket1:
    print(fruit)
print("************")

for i in range(len(fruit_basket2)):
    print(fruit_basket2[i])
