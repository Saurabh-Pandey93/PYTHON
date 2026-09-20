num = int(input("Enter a number: "))
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

if start <= num <= end:
    print(f"{num} lies within {start} to {end}")
else:
    print(f"{num} does NOT lie within {start} to {end}")