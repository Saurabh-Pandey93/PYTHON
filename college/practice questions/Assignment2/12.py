username = input("enter username:")
password = input("enter password:")

if (username == "admin" and password == "pass"):
    print("LOGIN SUCCESSFUL!")
elif (username != "admin"):
    print("wrong Username")
else:
    print("Wrong Password")