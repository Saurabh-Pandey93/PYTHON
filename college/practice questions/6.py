base_price = int(input("Enter the base price of item:"))
GST = base_price*0.18
total_amount = GST + base_price
print("The amount after taxes are:", total_amount)