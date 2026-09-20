class Students:
    college_name = "BBDIT" #class

    def __init__(self, name, cgpa):
        self.name = name #instance
        self.cgpa = cgpa


stu1 = Students("Saurabh Pandey", 9.3)

print(stu1.name)
print(Students.college_name)
        