# Accept a string and check if it's a valid password (at least 1 uppercase, 1 digit, and 1 special character)

password = input("Enter a password: ")

has_upper = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    if char.isdigit():
        has_digit = True
    if char in ['@', '_', '#']:
        has_special = True

if has_upper and has_digit and has_special:
    print("Valid password")
else:
    print("Invalid password: Must contain at least one uppercase letter, one digit, and one special character (@, _, #)")
