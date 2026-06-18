# A secure login simulation that asks for a username and password, 
# and checks them against a prerefined list of valid credentials.

login_details = {}

while True:
    username = input("Enter 'quit' to exit or enter your username: ")

    if username.lower() == 'quit':
        print("\n*****Exiting the login simulation.*****")
        break
    elif username.strip() == "":
        print("\n-Username cannot be empty. Please try again.")
        continue
    elif username in login_details:
        print("\n-Username already exists. Please choose a different username.")
        continue

    while True:
        print("\n-Password must be at aleast 4 caracters long.")
        password = input("\nEnter your password: ")
        if len(password) < 4:
            print("\nPassword is too short.Please try again.")
            continue
        
        confirm_password = input("Confirm your password: ")
        if password != confirm_password:
            print("\n-Passwords do not match. Please try again.")
            continue
        else:
            break

    login_details[username] = password
    print(f"\nAccount created successfully for username: {username}")

# Let the user try to log in with the created credentials
print("\n*****Login Simulation*****")
while True:
    username = input("Enter your username to log in (or 'quit' to exit)")
    if username.lower() == 'quit':
        print("\n*****Exiting the login simulation.*****")
        break
    elif username.strip() == "":
        print("\n-Please enter a valid username.")
        continue
    elif username not in login_details:
        print("\n-Username not found. Please try again.")
        continue
    while True:
        password = input("Enter your password: ")
        if password == login_details[username]:
            print(f"\nLogin successful! Welcome, {username}.")
            break
        else:
            print("\n-Invalid password. Please try again.")