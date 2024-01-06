class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

dog1 = Dog("Tom", 12)
dog1.set_name("Candy")
print(dog1.get_name())
print(dog1.age)
print(dog1.name)