username = input("enter username:")
password = input("enter password:")

if(username == "admin" and password == "pass"):
    print("correct password")
else:
    if(username != "admin"):
        print("wrong username")
    else:
        print("wrong password")