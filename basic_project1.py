
print("USER INFORMATION VALIDATOR")
print("--------------------------")

name = input("Enter your name: ")
email = input("Enter your email: ")
age = input("Enter your age: ")

errors = []

# Name validations :  without follow than print these messages 
if len(name) < 3:
    errors.append("Name must have at least 3 characters.") #append use in add element,name 
if not name[0].isalpha():
    errors.append("Name must start with a letter.")

# Email validations : without follow than print these messages 
if "@" not in email:
    errors.append("Email must contain '@'.")
if not email.endswith(".com"):
    errors.append("Email must end with .com")

# Age validations : without follow than print these messages 
if not age.isdigit():
    errors.append("Age must be a number.")
else:
    age = int(age)
    if age < 0:
        errors.append("Age cannot be negative.")
    elif age < 18:
        errors.append("User must be 18 or older.")

# Final output
if len(errors) == 0:
    user = (name, email, age)
    print("User information saved:", user) #success output when all codition follow
else:
    print("Errors found:") #error output when any condition not follow     
    print(errors)
