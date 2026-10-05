students = [
    {"roll": 1, "name": "Aarav", "marks": 85},
    {"roll": 2, "name": "Priya", "marks": 92},
    {"roll": 3, "name": "Rohan", "marks": 78},
    {"roll": 4, "name": "Ananya", "marks": 92},
    {"roll": 5, "name": "Vikram", "marks": 65}
]   
top_scorers = [s for s in students if s["marks"] > 80]
for s in top_scorers:
    print(s["name"], s["marks"])
