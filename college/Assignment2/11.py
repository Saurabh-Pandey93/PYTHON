num = int(input("Enter a number: "))
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

if start <= num <= end:
    if num % 3 == 0:
        print("The number is divisible by 3")
    else:
        print("Not divisible by 3")