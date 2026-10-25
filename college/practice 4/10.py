def temp_converter(C):
    return f"The temperature in Fahreinheit is {(C*9/5)+32}"
  
C = float(input("Enter the temperature in Celsius : "))

print(temp_converter(C))