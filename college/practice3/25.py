phone_book = {
    "Aarav": "9876543210",
    "Priya": "9123456789",
    "Rohan": "9988776655",
    "Ananya": "9012345678"
}

# Search
name = input("Enter name: ")  # Priya
if name in phone_book:
    print(f"{name}: {phone_book[name]}")
else:
    print("Not found")

# Add
phone_book["Vikram"] = "9765432109"

# Delete
del phone_book["Rohan"]

# List all
for name, number in phone_book.items():
    print(f"{name}: {number}")   