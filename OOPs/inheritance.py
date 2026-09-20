class Employee:
    start_time = "9AM"
    end_time = "5PM"

    def change_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher (Employee):
    def _init_(self, subject):
        self.subject = subject
        

t1 = Teacher("maths")
t1.change_time("4PM")


print(t1.subject, t1.start_time, t1.end_time)