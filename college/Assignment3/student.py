
students = [
    {"roll_no": 101, "name": "Rahul", "marks": 85},
    {"roll_no": 102, "name": "Aman", "marks": 42},
    {"roll_no": 103, "name": "Priya", "marks": 95},
    {"roll_no": 104, "name": "Rohit", "marks": 78},
    {"roll_no": 105, "name": "Neha", "marks": 67},
    {"roll_no": 106, "name": "Vikas", "marks": 32},
    {"roll_no": 107, "name": "Anjali", "marks": 88},
    {"roll_no": 108, "name": "Karan", "marks": 56},
    {"roll_no": 109, "name": "Sneha", "marks": 91},
    {"roll_no": 110, "name": "Arjun", "marks": 50}
]

PASSING_MARKS = 40


# 1. Display all students
def display_students():
    print("\n========== ALL STUDENTS ==========")
    print(f"{'Roll No':<12}{'Name':<15}{'Marks':<10}")
    print("-" * 37)

    for student in students:
        print(
            f"{student['roll_no']:<12}"
            f"{student['name']:<15}"
            f"{student['marks']:<10}"
        )


# 2. Find the student with the highest marks
def highest_marks():
    student = max(students, key=lambda s: s["marks"])
    print("\n========== HIGHEST MARKS ==========")
    print(f"Name: {student['name']}")
    print(f"Roll No: {student['roll_no']}")
    print(f"Marks: {student['marks']}")


# 3. Find the student with the lowest marks
def lowest_marks():
    student = min(students, key=lambda s: s["marks"])
    print("\n========== LOWEST MARKS ==========")
    print(f"Name: {student['name']}")
    print(f"Roll No: {student['roll_no']}")
    print(f"Marks: {student['marks']}")


# 4. Calculate average marks
def average_marks():
    average = sum(s["marks"] for s in students) / len(students)
    print(f"\nAverage Marks: {average:.2f}")


# 5. Display students scoring above 80
def students_above_80():
    print("\n========== STUDENTS ABOVE 80 ==========")

    found = False

    for student in students:
        if student["marks"] > 80:
            print(f"{student['name']} - {student['marks']}")
            found = True

    if not found:
        print("No students scored above 80.")


# 6. Search student by roll number
def search_student():
    try:
        roll = int(input("Enter roll number to search: "))

        for student in students:
            if student["roll_no"] == roll:
                print("\nStudent Found!")
                print(f"Roll No: {student['roll_no']}")
                print(f"Name: {student['name']}")
                print(f"Marks: {student['marks']}")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid roll number.")


# 7. Count students who passed and failed
def count_pass_fail():
    passed = sum(
        1 for s in students if s["marks"] >= PASSING_MARKS
    )
    failed = len(students) - passed

    print("\n========== PASS / FAIL REPORT ==========")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")


# 8. Sort students by marks
def sort_by_marks():
    sorted_students = sorted(
        students, key=lambda s: s["marks"], reverse=True
    )

    print("\n========== STUDENTS SORTED BY MARKS ==========")

    for student in sorted_students:
        print(f"{student['name']} - {student['marks']}")


# 9. Display names in alphabetical order
def alphabetical_names():
    names = sorted(s["name"] for s in students)

    print("\n========== ALPHABETICAL ORDER ==========")

    for name in names:
        print(name)


# 10. Display complete summary
def student_summary():
    total = len(students)
    average = sum(s["marks"] for s in students) / total

    highest = max(students, key=lambda s: s["marks"])
    lowest = min(students, key=lambda s: s["marks"])

    passed = sum(
        1 for s in students if s["marks"] >= PASSING_MARKS
    )
    failed = total - passed

    above_80 = [
        s["name"] for s in students if s["marks"] > 80
    ]

    print("\n========== STUDENT REPORT ==========")
    print(f"Total Students: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest: {highest['name']} - {highest['marks']}")
    print(f"Lowest: {lowest['name']} - {lowest['marks']}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print("Students Above 80:", ", ".join(above_80))


# Main menu
def main():
    while True:
        print("""
=====================================
       STUDENT DATABASE ANALYZER
=====================================
1. Display All Students
2. Find Highest Marks
3. Find Lowest Marks
4. Calculate Average Marks
5. Students Scoring Above 80
6. Search Student by Roll Number
7. Count Passed and Failed Students
8. Sort Students by Marks
9. Display Names Alphabetically
10. Display Student Summary
0. Exit
=====================================
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students()
        elif choice == "2":
            highest_marks()
        elif choice == "3":
            lowest_marks()
        elif choice == "4":
            average_marks()
        elif choice == "5":
            students_above_80()
        elif choice == "6":
            search_student()
        elif choice == "7":
            count_pass_fail()
        elif choice == "8":
            sort_by_marks()
        elif choice == "9":
            alphabetical_names()
        elif choice == "10":
            student_summary()
        elif choice == "0":
            print("Exiting Student Database Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 0 to 10.")


if __name__ == "__main__":
    main()
