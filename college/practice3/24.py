students = [
    {"roll": 1, "name": "Aarav", "marks": 85},
    {"roll": 2, "name": "Priya", "marks": 92},
    {"roll": 3, "name": "Rohan", "marks": 78},
    {"roll": 4, "name": "Ananya", "marks": 92},
    {"roll": 5, "name": "Vikram", "marks": 65}
]   

roll = int(input("Enter roll number: "))  # 3

found = [s for s in students if s["roll"] == roll]
if found:
    print(found[0]["name"], found[0]["marks"])  # Rohan 78
else:
    print("Not found")   