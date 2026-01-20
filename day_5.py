import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword generator!")
no_letters=int(input("How many letters would you like in your password?"))
no_symbols=int(input("How many symbols would you like?"))
no_nums=int(input("How many numbers would you like?"))

password_list=[]

for char in range(0,no_letters):
    password_list.append(random.choice(letters))
for char in range(0,no_symbols):
    password_list.append(random.choice(symbols))
for char in range(0,no_nums):
    password_list.append(random.choice(numbers))

print(password_list)

password=""
for i in password_list:
    password+=i
print(f"Simple password is {password}")

random.shuffle(password_list)

shu_pass=""
for i in password_list:
    shu_pass+=i
print(f"hardest password is {shu_pass}")

