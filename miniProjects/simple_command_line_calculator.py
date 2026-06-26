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