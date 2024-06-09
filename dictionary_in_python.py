tel = {'jack' : 4098, 'sape' : 4097}
tel['guido'] = 4099 # will add item to tel dictionary
print(tel)
print(tel['jack']) # get the value for key that is passed
del tel['jack'] # delete key value pair from dictionary
print(tel)
tel['irv'] = 4100
print(tel)
print(list(tel)) # prints list of keys in order of insertion
print(sorted(tel)) # prints list of keys in sorted order
print('guido' in tel)
print('jack' in tel)
print('sape' not in tel)

# dictionary comprehensions
print({x: x**2 for x in range(10) if x % 2 == 0}) # print squares of even numbers between 0 and 10

# Looping Techniques
knights = {'gallahad' : 'the pure', 'robin' : 'the brave'}
for k, v in knights.items():
    print(k,v)

for i, v in enumerate(['tic','tac','toe']):
    print(i, v)

questions = ['name', 'quest', 'favourite color']
answers = ['Lancelot', 'the holy grail', 'blue']
for q, a in zip(questions,answers):
    print(f"What is your {q}? It is {a}.")
    # print("What is your {0}? It is {1}.".format(q,a))

# Loop over sequence in reversed order
for i in reversed(range(1, 10, 2)):
    print(i)

# loop over sequence in sorted order
basket = ["apples","oranges","apricots","green apple","oranges","pear","chickoo"]
for fruit in sorted(basket):
    print(fruit)

# loop over unique elements of squence in sorted order
for fruit in sorted(set(basket)):
    print(fruit)

print(list(enumerate(basket)))
print(type(list(enumerate(basket))))
print(any())
