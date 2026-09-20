class Student:
   def __init__(self, name, cgpa):  # double underscores
       self.name = name 
       self.cgpa = cgpa
    
stu1 = Student("Rahul", 7.0)
stu2 = Student("Saurabh", 9.3)
stu3 = Student("Naval", 8.0)

print(stu1.cgpa)  # 7.0
print(stu2.name)  # Saurabh
print(stu3.name)  # Naval