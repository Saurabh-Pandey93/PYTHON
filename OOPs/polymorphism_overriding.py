class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designated(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()