def authenticate_password():
    correct_password = "secret123"  
    while True:
        user_input = input("Enter password: ")
        if user_input == correct_password:
            print("Access granted!")
            return True  
        else:
            print("Incorrect password. Try again.")


authenticate_password()   