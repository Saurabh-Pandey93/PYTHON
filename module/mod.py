import random

def generate_otp():
    return str(random.randint(1000, 9999))

def send_otp(email, otp):
    print(f"OTP sent to {email}: {otp}")

def verify_otp(entered, correct):
    return entered == correct   