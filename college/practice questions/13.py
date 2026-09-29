Weight = float(input("Enter the weight of the person (in kg):  "))
Height_provided = float(input("Enter the height of the person (in feet):  "))
Height = Height_provided/3.28

BMI = Weight/(Height**2)
print("The BMI of the person is:  ", BMI)
if BMI <= 18.5:
    print("Underweight")

elif 18.5 < BMI <= 29.5:
    print("Normal weight")
else:
    print("obese")