import random 
import string

print("Welcome to the password generator! I will ask you a few questions to create a secure password for you.")
upper  = input("Do you want lowercase letters in your password? (yes/no):").strip().lower()
length = int(input("How long do you want your password to be? (8-16 characters):"))
lower = input("Do you want lowercase letters in your password? (yes/no):").strip().lower()
numbers = input("Do you want to include numbers in your password? (yes/no):").strip().lower()
symbols = input("Do you want to include symbols in your password? (yes/no):").strip().lower()

def generate_password(length,lower,upper,numbers,symbols):
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    number_chars = string.digits
    symbol_chars = string.punctuation
    available_chars = ""
    password = ""
    
    if lower == 'yes':
        available_chars += lower_chars
    if upper == 'yes':
        available_chars += upper_chars
    if numbers == 'yes':
        available_chars += number_chars
    if symbols == 'yes':
        available_chars += symbol_chars
    if not available_chars:
        print("You must select at least one character type for your password.")
        return
    for i in range(length):
        password += random.choice(available_chars)
    print(f"Your generated password is: {password}")
    
    
   

generate_password(length, lower, upper, numbers, symbols)    
