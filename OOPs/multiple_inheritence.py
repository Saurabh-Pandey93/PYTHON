class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Students:
    def __init__(self, cgpa):
        self.cgpa = cgpa

class TA(Teacher, Students):
    def __init__(self, salary, cgpa, name):
        super().__init__(salary)
        Students.__init__(self, cgpa)
        self.name = name

ta1 = TA(15_0000, 9.3, "Saurabh Pandey")

print(ta1.name, ta1.cgpa, ta1.salary)