
from mod import generate_otp, send_otp, verify_otp

def login(email):
    otp = generate_otp()
    send_otp(email, otp)

    for attempt in range(1, 6):
        entered = input(f"Enter OTP (attempt {attempt}/5): ")
        if verify_otp(entered, otp):
            print("Login successful!")
            return
        print("Wrong OTP.")

    print("User is blocked")

email = input("Enter email: ")
login(email)   