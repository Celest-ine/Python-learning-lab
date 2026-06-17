# A secure login simulation that asks for a username and password, 
# and checks them against a prerefined list of valid credentials.

login_details = {}

while True:
    username = input("Enter 'quit' to exit or enter your username: ")

    if username.lower() == 'quit':
        print("Exiting the login simulation.")
        break

    print("Your password must be at least 4 characters long.")
    password = input("Enter your password: ")
    if len(password) < 4:
        print("Password is too short.Please try again.")
        continue

    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        continue

    login_details[username] = password
    print(f"Account created successfully for username: {username}")
