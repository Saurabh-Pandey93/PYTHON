def EvenOdd(a):
    if a % 2 == 0:
        return "The number is Even"
    else:
        return "The number is Odd"
a = int(input("Enter the number to be checked : "))
print(EvenOdd(a))
    