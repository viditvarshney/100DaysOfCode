import random
import string
letters = string.ascii_letters

numbers = string.digits
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ''
for i in range(nr_letters):
    password = password + random.choice(letters)

for i in range(nr_symbols):
    password = password + random.choice(numbers)

for i in range(nr_symbols):
    password = password + random.choice(symbols)

print(''.join(random.sample(password, len(password))))
