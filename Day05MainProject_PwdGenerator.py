import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
number_of_letters=int(input("How many letters would you like in your password?\n"))
number_of_numbers=int(input("How many numbers would you like?\n"))
number_of_symbols=int(input("How many symbols would you like?\n"))

letters_length=len(letters)
numbers_length=len(numbers)
symbols_length=len(symbols)

password = ""
password_list=[]

for letter in range(0,number_of_letters) :
    random_letter_index=random.randint(0,len(letters)-1)
    password += letters[random_letter_index]
    

for number in range(0,number_of_numbers) :
    random_number_index=random.randint(0,len(numbers)-1)
    password += numbers[random_number_index]

for symbol in range(0,number_of_symbols) :
    random_symbol_index=random.randint(0,len(symbols)-1)
    password += symbols[random_symbol_index]

new_password = ""

for ch in range(0,len(password)) :
    random_ch_index=random.randint(0,len(password)-1)
    new_password+=password[random_ch_index]

print(f"Your password : {new_password}")

# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password = []

# for _ in range(nr_letters):
#   password.append(random.choice(letters))

# for _ in range(nr_symbols):
#   password.append(random.choice(symbols))

# for _ in range(nr_numbers):
#   password.append(random.choice(numbers))

# random.shuffle(password)

# print('Your new password is : \n')
# print(*password, sep='')
