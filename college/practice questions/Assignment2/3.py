Year = int(input("Enter the Year to be checked"))
if Year%400 == 0 :
    print("The year is leap year")

elif Year%100 == 0:
    print("Not a leap year ")
elif Year%4 == 0:
    print("The year is leap year")

else:
    print("Not a leap year")