import random
letters=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
      't','u','v','w','x','y','z')
symbol=('!','@','#','$','%','^','&','*','(',')')
numbers=('1','2','3','4','5','6','7','8','9','0')

print("Welcome to password generator")
n_letters=int(input("Enter how many letters would you like to add in your password:"))
n_symbol=int(input("Enter how many symbols would you like to add in your password:"))
n_numbers=int(input("Enter how many numbers would you like to add in your password:"))

password_list=[]
for char in range(0,n_letters):
    password_list.append(random.choice(letters))
for char in range(0,n_symbol):
    password_list.append(random.choice(symbol))
for char in range(0,n_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password += char

print(f"Your password is:{password}")

