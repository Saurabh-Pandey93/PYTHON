students = [
    {"roll": 1, "name": "Aarav", "marks": 85},
    {"roll": 2, "name": "Priya", "marks": 92},
    {"roll": 3, "name": "Rohan", "marks": 78},
    {"roll": 4, "name": "Ananya", "marks": 92},
    {"roll": 5, "name": "Vikram", "marks": 65}
]   

avg = sum(s["marks"] for s in students) / len(students)
print(f"Average: {avg}")  