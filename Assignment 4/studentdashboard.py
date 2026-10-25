
students = []

SUBJECTS = ["Python", "DBMS", "OS", "Maths", "CN"]


# 1. Add Student
def add_student():
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty!")
            return

        roll = int(input("Enter roll number: "))

        if any(student["roll"] == roll for student in students):
            print("Roll number already exists!")
            return

        marks = []

        for subject in SUBJECTS:
            while True:
                try:
                    mark = float(input(f"Enter marks in {subject}: "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

        student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    except ValueError:
        print("Please enter a valid roll number.")


# 2. Display Students
def display_students():
    if not students:
        print("No student records available.")
        return

    print("\n========== STUDENT LIST ==========")
    print(f"{'Roll':<10}{'Name':<20}{'Total':<10}{'Percentage':<12}")

    for student in students:
        total = calculate_total(student)
        percentage = calculate_percentage(student)

        print(
            f"{student['roll']:<10}"
            f"{student['name']:<20}"
            f"{total:<10.1f}"
            f"{percentage:.2f}%"
        )


# 3. Search Student
def search_student():
    try:
        roll = int(input("Enter roll number to search: "))

        student = next(
            (s for s in students if s["roll"] == roll),
            None
        )

        if student:
            display_result(student)
        else:
            print("Student not found.")

    except ValueError:
        print("Enter a valid roll number.")


# 4. Calculate Total Marks
def calculate_total(student):
    return sum(student["marks"])


# 5. Calculate Percentage
def calculate_percentage(student):
    total = calculate_total(student)
    return total / len(SUBJECTS)


# 6. Calculate Grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


# Display an individual student's result
def display_result(student):
    total = calculate_total(student)
    percentage = calculate_percentage(student)
    grade = calculate_grade(percentage)

    print("\n========== STUDENT RESULT ==========")
    print(f"Name        : {student['name']}")
    print(f"Roll Number : {student['roll']}")
    print("------------------------------------")

    for subject, mark in zip(SUBJECTS, student["marks"]):
        print(f"{subject:<12}: {mark:g}")

    print("------------------------------------")
    print(f"Total       : {total:g} / 500")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print("====================================")


# 7. Find Topper
def find_topper():
    if not students:
        print("No student records available.")
        return

    topper = max(students, key=calculate_percentage)

    print("\n========== CLASS TOPPER ==========")
    print(f"Name       : {topper['name']}")
    print(f"Roll       : {topper['roll']}")
    print(f"Percentage : {calculate_percentage(topper):.2f}%")
    print(f"Grade      : {calculate_grade(calculate_percentage(topper))}")


# 8. Display Class Statistics
def display_statistics():
    if not students:
        print("No student records available.")
        return

    percentages = [calculate_percentage(s) for s in students]
    topper = max(students, key=calculate_percentage)

    passed = sum(1 for p in percentages if p >= 40)
    failed = len(students) - passed

    print("\n========== CLASS STATISTICS ==========")
    print(f"Total Students       : {len(students)}")
    print(f"Class Average        : {sum(percentages) / len(percentages):.2f}%")
    print(f"Highest Percentage   : {max(percentages):.2f}%")
    print(f"Lowest Percentage    : {min(percentages):.2f}%")
    print(f"Topper               : {topper['name']}")
    print(f"Students Passed      : {passed}")
    print(f"Students Failed      : {failed}")


# 9. Sort Students by Percentage
def sort_students():
    if not students:
        print("No student records available.")
        return

    sorted_students = sorted(
        students,
        key=calculate_percentage,
        reverse=True
    )

    print("\n====== STUDENTS SORTED BY PERCENTAGE ======")

    for student in sorted_students:
        print(
            f"{student['name']} | Roll: {student['roll']} | "
            f"Percentage: {calculate_percentage(student):.2f}%"
        )


# 10. Delete Student
def delete_student():
    try:
        roll = int(input("Enter roll number to delete: "))

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Enter a valid roll number.")


# 11. Update Student Marks
def update_student_marks():
    try:
        roll = int(input("Enter roll number: "))

        student = next(
            (s for s in students if s["roll"] == roll),
            None
        )

        if student is None:
            print("Student not found.")
            return

        print(f"Updating marks for {student['name']}")

        for i, subject in enumerate(SUBJECTS):
            while True:
                try:
                    mark = float(
                        input(f"Enter new marks for {subject}: ")
                    )

                    if 0 <= mark <= 100:
                        student["marks"][i] = mark
                        break
                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

        print("Marks updated successfully!")

    except ValueError:
        print("Enter a valid roll number.")


# 12. Display Students Scoring Above 80%
def students_above_80():
    found = False

    print("\n====== STUDENTS SCORING ABOVE 80% ======")

    for student in students:
        percentage = calculate_percentage(student)

        if percentage > 80:
            print(
                f"{student['name']} | Roll: {student['roll']} | "
                f"Percentage: {percentage:.2f}%"
            )
            found = True

    if not found:
        print("No students scored above 80%.")


# Main Menu
def main():
    while True:
        print("""
==================================
     STUDENT PERFORMANCE SYSTEM
==================================
1. Add Student
2. Display Students
3. Search Student
4. Student Result
5. Find Topper
6. Class Statistics
7. Sort Students by Percentage
8. Delete Student
9. Update Student Marks
10. Show Students Scoring Above 80%
11. Exit
==================================
""")

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            try:
                roll = int(input("Enter roll number: "))
                student = next(
                    (s for s in students if s["roll"] == roll),
                    None
                )

                if student:
                    display_result(student)
                else:
                    print("Student not found.")

            except ValueError:
                print("Enter a valid roll number.")

        elif choice == "5":
            find_topper()

        elif choice == "6":
            display_statistics()

        elif choice == "7":
            sort_students()

        elif choice == "8":
            delete_student()

        elif choice == "9":
            update_student_marks()

        elif choice == "10":
            students_above_80()

        elif choice == "11":
            print("Thank you for using Student Performance System!")
            break

        else:
            print("Invalid choice! Please select from 1 to 11.")


if __name__ == "__main__":
    main()
