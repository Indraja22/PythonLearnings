import random, string

class RandomPasswordGenerator:
    def generate_random_password(self,length):
        special_chars = ["#","@","$","&"]
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        password = ''.join(random.choice(letters) for i in range(length))
        print(password+random.choice(special_chars))

random_password_gen = RandomPasswordGenerator()
random_password_gen.generate_random_password(10)      