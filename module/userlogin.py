import random
otp = random.randint(1000, 9999)
otp = 1111
enter_otp = int(input("enter the OTP :"))
entered_otp = enter_otp
while True:
    if otp == entered_otp:
        print("login successful")
        break
    else:
        entered_otp = int(input("wrong!!, Enter again : "))   