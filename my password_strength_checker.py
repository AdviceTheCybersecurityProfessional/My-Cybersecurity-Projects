def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return "Strong: Password contains both letters and numbers."
    else:
        return "Moderate: Password is of moderate strength."

# Get user input for password
user_password = input("Enter your password: ")
result = check_password_strength(user_password)

# Display the result
print(result)
python password_strength_checker.py
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return "Strong: Password contains both letters and numbers."
    else:
        return "Moderate: Password is of moderate strength."

# Password to check
user_password = "Forex19@"

# Display the result
result = check_password_strength(Forex19@)
Strong:Password contains both letters and numbers
