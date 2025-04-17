#To get password from a user
password = input("Enter your password: ")

# Counting the number of passed checked from "0"
passed_checks = 0

#Check 1: To check for the password length
if len(password) >= 8:
    passed_checks += 1
else:
    print("At least 8 characters needed")

#Check 2: To check for at least one lowercase letter
has_lowercase = False 
for character in password:
    if character.islower():
        has_lowercase = True
        break
if has_lowercase: 
    passed_checks += 1
else:
    print("Password should have at least a lowercase letter")

#Check 3: To check for at least one uppercase lettrr
has_uppercase = False
for character in password:
    if character.isupper():
        has_upper = True
        break

if has_uppercase:
    passed_checks += 1
else:
    print("Password should contain at least one uppercase letter")

    
#Check 4: To check for at least a digit
has_digit = False
for character in password:
    if character.isdigit: 
        has_digit = True

if has_digit:
    passed_checks += 1
else:
    print("Password should have at least one number")
    

#Check 5: To check for special characters
special_characters = "!@#$%&*^=~_"
has_special_character = False 
for character in password:
    if character in special_characters:
        has_special_character = True
        break

if has_special_character:
    passed_checks += 1
else:
    print("Password should have at least one special character")


# To check for the password strength
if passed_checks == 5:
    strength = "Strong"
elif passed_checks >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print ("Password Strength:", strength)

