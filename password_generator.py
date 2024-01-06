'''
Password length : 8 to 40
Include atleast 1 symbol
Include atleast 1 uppercase
Include atleast 1 number
'''
import string
import random

password_len = 12
password = ""

letters_uppercase = string.ascii_uppercase
letters_lowercase = string.ascii_lowercase
digits = string.digits
special_chars = '@#!$%'

combined = letters_uppercase + letters_lowercase + digits + special_chars
combined_list = list(combined)

rand_letters_lowercase = random.choice(letters_lowercase)
rand_letters_uppercase = random.choice(letters_uppercase)
rand_digits = random.choice(digits)
rand_special_chars = random.choice(special_chars)

temp_password = rand_letters_lowercase + rand_letters_uppercase + rand_digits + rand_special_chars

for i in range(0, password_len - 4):
    temp_password =  temp_password + random.choice(combined_list)
    temp_password_list = list(temp_password)
    random.shuffle(temp_password_list)

password = "".join(temp_password_list)

print(password)