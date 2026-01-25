correct_username = "python"
correct_password = "rules"

max_attempts = 5
attempts = 0

logged_in = False

while attempts < max_attempts and not logged_in:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        logged_in = True
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Incorrect username or password. Please try again.")

if logged_in:
    print("Welcome")
else:
    print("Access denied")
