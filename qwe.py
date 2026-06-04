password = input("Enter Password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
if any(char.isupper() for char in password):
    score += 1

# Lowercase check
if any(char.islower() for char in password):
    score += 1

# Number check
if any(char.isdigit() for char in password):
    score += 1

# Special character check
special_chars = "@#$%^&+=!"
if any(char in special_chars for char in password):
    score += 1

# Strength result
print("\nPassword Strength:")

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")