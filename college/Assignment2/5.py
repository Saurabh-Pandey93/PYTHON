Purchased_Amount = float(input("Enter the Amount Spent :"))
Deducted_Amount = Purchased_Amount*0.15
if Purchased_Amount >= 2000:
    print("The amount to be deducted is :", Deducted_Amount)
else:
    print("No Discount is Available")