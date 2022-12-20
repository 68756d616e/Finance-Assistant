# Finance Assistant 

# Welcome message for users
print("Welcome to your finance assistant")

# The tax bracket definition and display message
def tax_bracket(salary):
    if salary <= 12000:
        tax_bracket = 20 # For future code
        print("You are not taxed nothing")
        return 'You can ask about tax brackets'
    elif salary >= 12001 and salary < 21999:
        tax_bracket = 10 # For future code
        print("You are taxed 10% yearly")
        return 'You can ask about tax brackets'
    elif salary >= 22000 and salary < 34999:
        tax_bracket = 20 # For future code
        print("You are taxed 20% yearly")
        return 'You can ask about tax brackets'
    elif salary >= 35000 and salary < 39999:
        tax_bracket = 30 # For future code
        print("You are taxed 30% yearly")  
        return 'You can ask about tax brackets'     
    else:
        tax_bracket = 40 # For future code
        print("You are taxed 40% yearly")
        return 'You can ask about tax brackets'

# Tax bracket category and display message - Example below, not accurate
def tax_types():
    if tax_bracket(salary):
        print("If you earn less than 12000 or equal to 12000, you do not pay tax ")
    if tax_bracket(salary):
        print("If you earn less than or equal to ")
    if tax_bracket(salary):
        print("If you earn less than or equal to ")
    if tax_bracket(salary):
        print("If you earn less than or equal to ")

# Salary of the user
salary = int(input("What is your yearly salary? "))

print(tax_bracket(salary))
question = input("Would you like to know all tax brackets? (y/n)")
if question == 'y':
    print(tax_types)
elif question == 'n':
    print("Ok, have a nice day")