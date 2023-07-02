# create a list
bikes = ['trek', 'giant', 'redline']

# first item in list
first_bike = bikes[0]
print(first_bike)

# last item in list
last_bike = bikes[-1]
print(last_bike)

# Loop through a list
for bike in bikes:
    print(bike)

# Adding items to a list
cycle = []
cycle.append("Mountain Bike")
cycle.append("street bike")
print(cycle)

# making numerical lists - squares of nums between 1 and 10
squares = []
for num in range(1, 11):
    squares.append(num**2)
print(squares)

# list comprehensions
squares_nm = [x**2 for x in range(1, 11)]
print(squares_nm)
even = [x for x in range(1, 101) if x % 2 == 0]
print(even)

# Slicing List
finishers = ['bob', 'aba', 'dea']
first_two = finishers[:2]
print(first_two)

# Copying List
copy_of_finishers = finishers[:]
print(copy_of_finishers)

copy_of_finishers = list(finishers)
print(copy_of_finishers)
