import math

def greetings():
    """Print a greeting message welcoming the user."""

    calculator_version = "Celestine's Calculator Version 1.0"

    #Capture username
    while True:
        user_name = input("Enter a user name you want to use in this session or Enter 'quit' to exit the session: ")
        
        if user_name.lower() == 'quit':
            print("\n***** Exiting Session ****")
            return
        
        elif user_name.strip() == "":
            print("\nYou need to enter a name please")
            continue
        
        elif user_name.isdigit():
            print("A number is not a valid name.Try again")
            continue
        break
    print(f"""\nHello, {user_name.title()} :)
          ***** WELCOME TO {calculator_version} *****
          """)

greetings()

# Operations carried out by the calculator

def multiplication(num1, num2):
    """Multiply two numbers."""
    return num1 * num2
def addition(num1, num2):
    """Add two numbers."""
    return num1 + num2
def subtraction(num1, num2):
    """Subtract the second number from the first number."""
    return num1 - num2
def division(num1, num2):
    """Divide the first number by the second number."""
    return num1 / num2
def modulo(num1, num2):
    """Find the remaider of the division of the first number and the second number."""
    return num1 %  num2
def power(num1,num2 ):
    """Raise the first number to the power of the second number."""
    return num1 ** num2
def squared(num1):
    """Return the result of a number multiplied by itself."""
    return num1 ** 2
def cubed(num1):
    """Return the result of a number cubed."""
    return num1 ** 3
def sqrroot(num1):
    """"Return the square root of a number."""
    return num1 ** 0.5
def percentage(part, whole):
    """Return the percentageof a number. """
    return (part / whole) * 100

def mathematical_operation():
    """Ask the user to enter the operation they want to perform."""
    options = ("""What mathematical operation do you want to perform:
                          1. Addition
                          2. Subtraction
                          3. Multiplication
                          4. Division
                          5. Modulo
                          6. Raise a number to the power of another number
                          7. Square a number
                          8. Cube a number
                          9. Find the squareroot of a number
                          10. Find the percentage of a number
                          11.Exit
                          """)
    print(options)
    
    while True:
        # Take user input
        choice = input("\nEnter your choice here: ")
        if choice == '11':
            print("\t\n*****Exiting Session***** ")
            break
        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("\nEnter the second number: "))
            if choice == '1':
                print(num1, '+', num2, '=', addition(num1, num2))
            elif choice == '2':
                print(num1, '-', num2, '=', subtraction(num1, num2))
            elif choice == '3':
                print(num1, '*', num2, '=', multiplication(num1, num2))
            elif choice == '4':
                print(num1, '/', num2, '=', division(num1, num2))
            elif choice == '5':
                print(num1, '%', num2, '=', modulo(num1, num2))
            elif choice == '6':
                print(num1, '**', num2, '=', power(num1, num2))
        elif choice in ('7', '8', '9'):
            num = float(input("\nEnter the number: "))
            if choice == '7':
                print(f"{num} squared is", squared(num))
            elif choice == '8':
                print(f"{num} cubed is", cubed(num))
            elif choice == '9':
                print(f"The square root of {num}", sqrroot(num))
        elif choice == '10':
            part = float(input("\nEnter the part number: "))
            whole = float(input("\nEnter the whole number: "))
            print(part, '*', whole, '/', '100 =', percentage(part, whole))
        else:
            print("Invalid input.Please enter the number of the operation you want to perform.")
            print(options)
            continue

mathematical_operation()