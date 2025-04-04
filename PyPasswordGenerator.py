# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:                         <----  Created by me ----->
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# # for i in range(0, nr_letters):
# #     password += letters[random.randint(0,len(letters)-1)]
# # for i in range(0, nr_symbols):
# #     password += symbols[random.randint(0,len(symbols)-1)]
# # for i in range(0, nr_numbers):
# #     password += numbers[random.randint(0,len(numbers)-1)]
# # print(password)

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# reqPass_length = nr_letters + nr_numbers + nr_symbols
# print(reqPass_length)
# while len(password) < reqPass_length:
#     choice = random.randint(1,3)
#     if choice == 1 and nr_letters > 0 :
#         password += letters[random.randint(0,len(letters)-1)]
#         nr_letters -= 1
#     elif choice == 2 and nr_symbols > 0:
#        password += symbols[random.randint(0,len(symbols)-1)] 
#        nr_symbols -= 1
#     elif nr_numbers == 3 and nr_numbers > 0:
#        password += numbers[random.randint(0,len(numbers)-1)] 
#        nr_numbers -= 1
# print(password)
# print(len(password))


#Password Generator Project 
import random

# Define available characters                                              "Optimize code "
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

# Gather user inputs
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create the password by randomly sampling the required characters
password = (
    random.choices(letters, k=nr_letters) +
    random.choices(symbols, k=nr_symbols) +
    random.choices(numbers, k=nr_numbers)
)

# Shuffle the password for randomness
random.shuffle(password)

# Convert list to string and display the result
print(f"Your password is: {''.join(password)}")
