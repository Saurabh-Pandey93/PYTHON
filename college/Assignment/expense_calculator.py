Name = input("Enter the Name :  ")
Monthly_Income = float(input("Enter the salary :  "))
Food_Expenses = float(input("Enter the amount spend on food :"))
Travel_Expenses = float(input("Enter the amount spend on travelling :  "))
Entertainment_Expenses = float(input("Enter the amount spend on entertainment :  "))
Other_Expenses = float(input("Enter the money spent on miscellaneous things: "))


Total_Expenses = Food_Expenses+Travel_Expenses+Entertainment_Expenses+Other_Expenses
print("Total Expense of the Individual:  ", Total_Expenses)

Remaining_Money = Monthly_Income - Total_Expenses
print("Remaining Money of the Month :", Remaining_Money)

Saving_Percentage = (Remaining_Money/Monthly_Income)*100
print("Saving of the Month is (in %):", Saving_Percentage)

Daily_Average_Spending = Total_Expenses/30
print(f"Daily Average Spending of the Salary is:{Daily_Average_Spending}")

Weekly_Average_Spending = Total_Expenses/4
print("Weekly Average Spending of the Salary is: ",Weekly_Average_Spending)

Saving_Target = int(input("Target is to save upto ( in %)"))
print("The Saving Target is (in %) : " ,Saving_Target)

if Saving_Target <= Saving_Percentage:
    print("Ihe Saving is Under My Target")

else:
    print("You Have to controllllll: ")

