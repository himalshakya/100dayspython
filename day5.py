import random
from datetime import datetime

random.seed(datetime.now().timestamp())

print("Welcome to the Password Generator!")
size = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

l_characters = [chr(c) for c in range(97, 123)]
u_characters = [chr(c) for c in range(65, 91)]
all_chars = l_characters + u_characters

numbers = [chr(c) for c in range(48, 58)]
symbols = [chr(c) for c in range(33, 48) if c != 34] # 34 == '"' or double quote

password_lst = []

for i in range(0, num_symbols):
  x = random.randint(0, len(symbols) - 1)
  password_lst.append(symbols[x])

for i in range(0, num_numbers):
  x = random.randint(0, len(numbers) - 1)
  password_lst.append(numbers[x])

remaining = size - num_numbers - num_symbols
for i in range(0, remaining):
  x = random.randint(0, len(all_chars) - 1)
  password_lst.append(all_chars[x])

random.shuffle(password_lst)
randomized_password = ''.join(password_lst)
print("Your password is: " + randomized_password)

# randomized_password = ""

# while len(password_lst) > 0:
#   x = random.randint(0, len(password_lst) - 1)
#   y = password_lst[x]
#   password_lst.remove(y)
#   randomized_password += y

# print("Here is your password: " + randomized_password)