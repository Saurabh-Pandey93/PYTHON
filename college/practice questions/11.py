Principle_amount = int(input("Enter the amount :"))
Rate = int(input("Enter the rate at which the interest will increase (in %)"))
Time = int(input("The time constraint is (in years): "))
Simple_interest = (Principle_amount*Rate*Time)/100
print("The simple interest of the amount is :", Simple_interest)