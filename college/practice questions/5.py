sub1 = int(input("Enter the marks obtained in sub1 :"))
Sub2 = int(input("Enter the marks obtained in sub2 :"))
sub3 = int(input("Enter the marks obtained in sub3 :"))
sub4 = int(input("Enter the marks obtained in sub4 :"))
Sub5 = int(input("Enter the marks obtained in sub5 :"))

Maximum_marks = 500
Total_marks = sub1+Sub2+sub3+sub4+sub4
print("Total Marks obtained by the student is:", Total_marks)

Percentage = Total_marks/Maximum_marks*100
print("Percentage of the Student is (in %):", Percentage)

if Percentage >= 40:
    print("Student is Qualified ")
else:
    print("failed")